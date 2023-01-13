import sys

sys.path.append('/Users/alex/PythonAQA')
print(sys.path)

from HW23.structure_without_list import StructureWithoutList

import pytest


@pytest.fixture()
def default_structure_without_list():
    structure_without_list = StructureWithoutList()
    return structure_without_list


def test_add_new_element(default_structure_without_list):
    default_structure_without_list.add(1)
    expected_value = 1
    expected_length = 1
    assert default_structure_without_list.get(1) == expected_value
    assert default_structure_without_list.length == expected_length


def test_add_two_elements(default_structure_without_list):
    default_structure_without_list.add(1)
    default_structure_without_list.add(2)
    expected_value_1 = 1
    expected_value_2 = 2
    expected_length = 2
    assert default_structure_without_list.get(1) == expected_value_1
    assert default_structure_without_list.get(2) == expected_value_2
    assert default_structure_without_list.length == expected_length


@pytest.mark.xfail(reason='Bug in method get')
def test_add_new_element_after_getting_element_by_index(default_structure_without_list):
    default_structure_without_list.add(11)
    default_structure_without_list.add(10)
    default_structure_without_list.add(55)
    default_structure_without_list.add(45)
    default_structure_without_list.add(75)
    default_structure_without_list.get(3)
    # default_structure_without_list.delete(3)
    default_structure_without_list.add(105)
    expected_value_by_index_4 = 45
    expected_value_by_index_6 = 105
    expected_length = 6
    assert default_structure_without_list.get(4) == expected_value_by_index_4
    assert default_structure_without_list.get(6) == expected_value_by_index_6
    assert default_structure_without_list.length == expected_length


@pytest.mark.xfail(reason='Bug in method delete')
def test_add_new_element_after_delete_this_element(default_structure_without_list):
    default_structure_without_list.add(11)
    default_structure_without_list.add(10)
    default_structure_without_list.add(55)
    default_structure_without_list.add(45)
    default_structure_without_list.add(75)
    default_structure_without_list.delete(3)
    default_structure_without_list.add(105)
    expected_value_by_index_3 = 45
    expected_value_by_index_5 = 105
    expected_length = 5
    assert default_structure_without_list.get(3) == expected_value_by_index_3
    assert default_structure_without_list.get(5) == expected_value_by_index_5
    assert default_structure_without_list.length == expected_length


def test_get_elements_in_fwd_dir(default_structure_without_list):
    default_structure_without_list.add(1)
    default_structure_without_list.add("second")
    default_structure_without_list.add(5)
    expected_length = 3
    assert default_structure_without_list.get(1) == 1
    assert default_structure_without_list.get(2) == "second"
    assert default_structure_without_list.get(3) == 5
    assert default_structure_without_list.length == expected_length


def test_get_zero_elements_from_non_empty_structure(default_structure_without_list):
    default_structure_without_list.add(1)
    default_structure_without_list.add("second")
    with pytest.raises(IndexError):
        default_structure_without_list.get(0)


def test_get_elements_from_empty_structure(default_structure_without_list):
    with pytest.raises(IndexError):
        default_structure_without_list.get(1)


def test_get_element_with_wrong_index_exception(default_structure_without_list):
    default_structure_without_list.add("second")
    with pytest.raises(IndexError):
        default_structure_without_list.get(10)


def test_delete_first_element(default_structure_without_list):
    default_structure_without_list.add(1)
    expected_value = None
    expected_length = 0
    assert default_structure_without_list.delete(1) == expected_value
    assert default_structure_without_list.length == expected_length


def test_delete_middle_element(default_structure_without_list):
    default_structure_without_list.add(4)
    default_structure_without_list.add(3)
    default_structure_without_list.add(5)
    expected_value_1 = 4
    expected_value_2 = 5
    expected_length = 2
    default_structure_without_list.delete(2)
    assert default_structure_without_list.get(1) == expected_value_1
    assert default_structure_without_list.get(2) == expected_value_2
    assert default_structure_without_list.length == expected_length


def test_delete_last_element(default_structure_without_list):
    default_structure_without_list.add(4)
    default_structure_without_list.add(3)
    default_structure_without_list.add(5)
    expected_value_1 = 4
    expected_value_2 = 3
    expected_length = 2
    default_structure_without_list.delete(3)
    assert default_structure_without_list.get(1) == expected_value_1
    assert default_structure_without_list.get(2) == expected_value_2
    assert default_structure_without_list.length == expected_length


def test_delete_all_elements(default_structure_without_list):
    default_structure_without_list.add(4)
    default_structure_without_list.add(3)
    default_structure_without_list.add(5)
    expected_length = 0
    for i in range(default_structure_without_list.length):
        default_structure_without_list.delete(1)

    assert default_structure_without_list.length == expected_length


def test_delete_element_with_existing_index(default_structure_without_list):
    default_structure_without_list.add(1)
    expected_value = None
    expected_length = 0
    assert default_structure_without_list.delete(1) == expected_value
    assert default_structure_without_list.length == expected_length


def test_delete_element_with_zero_index(default_structure_without_list):
    default_structure_without_list.add(1)
    with pytest.raises(IndexError):
        default_structure_without_list.delete(0)


def test_delete_element_with_wrong_index_exception(default_structure_without_list):
    with pytest.raises(IndexError):
        default_structure_without_list.delete(10)
