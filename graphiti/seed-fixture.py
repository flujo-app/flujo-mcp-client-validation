"""Seed one disposable Graphiti episode directly; no model inference."""
import asyncio
import json
from datetime import datetime, timezone
from graphiti_core.driver.falkordb_driver import FalkorDriver
from graphiti_core.nodes import EpisodeType, EpisodicNode

async def main():
    driver = FalkorDriver(host="127.0.0.1", port=6379, database="flujo_listing_fixture")
    node = EpisodicNode(
        uuid="6e0b6a02-6f11-4ad0-a2dc-675f803b4420",
        name="FLUJO local read-only fixture",
        group_id="flujo-listing-test",
        source=EpisodeType.text,
        source_description="Disposable client validation fixture seeded directly through Graphiti core; no model inference",
        content="This harmless local fixture verifies Graphiti episode retrieval through the FLUJO MCP Tool Tester.",
        valid_at=datetime.now(timezone.utc),
    )
    await node.save(driver)
    print(json.dumps({"uuid": node.uuid, "name": node.name, "group_id": node.group_id, "content": node.content}))
    await driver.close()

asyncio.run(main())
