# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    # test logical error for backstage pass with <=10 sell in days should
    # increase quality by 2
    def test_backstage_pass_should_increase_quality_sell_in_leq_10(self):
        items = [Item("Backstage passes", 8, 30)]
        backstage_pass_item = items[0]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(32, backstage_pass_item.quality)

    # test logical error for backstage pass with <=3 sell in days should
    # increase quality by 3
    def test_backstage_pass_should_increase_quality_sell_in_leq_5(self):
        items = [Item("Backstage passes", 3, 30)]
        backstage_pass_item = items[0]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(33, backstage_pass_item.quality)

    # test logical error for backstage pass quality should be 0 after concert
    # date
    def test_backstage_pass_quality_drop_zero_after_concert_date(self):
        items = [Item("Backstage passes", 0, 50)]
        backstage_pass_item = items[0]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, backstage_pass_item.quality)

    # test logical error with invalid starting quality over 50
    # should yield 50
    def test_out_of_bounds_starting_quality_over(self):
        items = [Item("Backstage passes", 1, 60)]
        backstage_pass_item = items[0]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertRaises(ValueError, lambda: backstage_pass_item.quality)

    # test logical error with invalid starting quality less than 0
    # should yield 0
    def test_out_of_bounds_starting_quality_under(self):
        items = [Item("Backstage passes", 1, -1)]
        backstage_pass_item = items[0]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertRaises(ValueError, lambda: backstage_pass_item.quality)

    # test syntax error for adding an item
    def test_gilded_rose_add_item(self):
        items = [Item("Backstage passes", 1, 30)]
        new_item = Item("Aged Brie", 5, 10)
        gilded_rose = GildedRose(items)
        gilded_rose.add_item(new_item)
        self.assertEquals(gilded_rose.items[1], new_item)


if __name__ == '__main__':
    unittest.main()
