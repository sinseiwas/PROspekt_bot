import unittest
from unittest.mock import AsyncMock
from answers import *
import asyncio


class TestMocking(unittest.IsolatedAsyncioTestCase):
    async def test_edit_trennings(self):
        message = AsyncMock()
        await cmd_edit_trennings(message)

        message.answer.assert_called_with('Успешно изменено')

    
    async def test_edit_cp(self):
        message = AsyncMock()
        await cmd_edit_content_plan(message)

        message.answer.assert_called_with('Успешно изменено')


    async def test_edit_cp(self):
        message = AsyncMock()
        await cmd_edit_director(message)

        message.answer.assert_called_with('Успешно изменено')


if __name__ == '__main__':
    unittest.main()
