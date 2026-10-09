"""FR-8: read-only MCP поверх ядра (официальный Python SDK, streamable-http).

Запуск: pip install -e ".[mcp]" && python -m engine.mcp_server
Запись на диск — запрещена (только run_check по запросу, без persistence).
"""

from __future__ import annotations


def create_server():
    from mcp.server import MCPServer  # extra-зависимость (см. pyproject [mcp])

    from .checks import check
    from .corpus import search, signals
    from .index import score

    mcp = MCPServer("agent-ready-engine")

    @mcp.tool()
    def search_corpus(query: str, limit: int = 10) -> list:
        """FTS-поиск по разборам/сигналам/глоссарию."""
        return search(query, limit)

    @mcp.tool()
    def get_system(slug: str) -> dict:
        """Разбор + сигналы + скор одной системы."""
        return {"score": score(slug), "signals": signals(slug)}

    @mcp.tool()
    def run_check(url: str, repo: str | None = None) -> dict:
        """Agent-Ready проверка URL (FR-3). Без записи на диск."""
        return check(url, repo)

    return mcp


def main() -> None:  # pragma: no cover
    import asyncio

    from mcp.server.stdio import stdio_server  # локально stdio; deploy — streamable-http

    async def _run():
        async with stdio_server() as (read, write):
            await create_server().run(read, write)

    asyncio.run(_run())


if __name__ == "__main__":
    main()
