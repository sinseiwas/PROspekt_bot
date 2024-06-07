from unittest.mock import AsyncMock

import pytest

from answers import cmd_edit_trennings


@pytest.mark.asyncio
async def test_edit_trennings():
    message = AsyncMock()
    await cmd_edit_trennings(message)

    message.answer.assert_called_with('Успешно изменено')