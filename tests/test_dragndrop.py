import pytest
from tests.base_test import BaseTest
from pages.dragndrop_page import DragNDropPage


class TestDragAndDrop(BaseTest):
    @pytest.mark.skip
    @pytest.mark.parametrize("number, expected_response",
                             [("1", ["Draggable 1"]),
                              ("2", ["Draggable 2"]),
                              ("all", ["Draggable 1", "Draggable 2"])])
    def test_first_drag_n_drop(self, number, expected_response):
        dragndrop_page = DragNDropPage(self.driver)
        dragndrop_page.change_to_drag_and_drop_page()
        dragndrop_page.drag_and_drop_first(number)
        actual_result = dragndrop_page.confirm_first_drop()
        assert actual_result == expected_response
