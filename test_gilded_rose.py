# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from gilded_rose import SubItem, AgedBrie, Sulfuras, BackstagePasses
from gilded_rose import NormalItem, Conjured


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Sulfuras("Sulfuras", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(50, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Sulfuras("Sulfuras", 5, 50)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(items, all_items)

    # test logical error with invalid starting quality less than 0
    # should raise error
    def test_out_of_bounds_starting_quality_under(self):
        with self.assertRaises(ValueError):
            items = [BackstagePasses("Backstage passes", 1, -1)]
            items.quality()

    # test logical error sell_in day of (technically not past sell_in day yet)
    # should not decrease quality by 2
    def test_boundary_sell_in_condition_quality_decrease_rate(self):
        items = [NormalItem("Banana", 0, 10)]
        banana_item = items[0]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, banana_item.quality)

    # test logical error of quality increase for Aged Brie behaves differently
    # at boundary condition
    def test_boundary_aged_brie_quality_increase_rate(self):
        items = [AgedBrie("Aged Brie", 1, 15)]
        aged_brie_item = items[0]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # this correctly passes, and adds one to quality
        self.assertEqual(16, aged_brie_item.quality)
        gilded_rose.update_quality()
        # this fails, since it adds two to quality, which is inconsistent
        self.assertEqual(17, aged_brie_item.quality)

    # test syntax error for adding an item
    def test_gilded_rose_add_item(self):
        items = [BackstagePasses("Backstage passes", 1, 30)]
        new_item = AgedBrie("Aged Brie", 5, 10)
        gilded_rose = GildedRose(items)
        gilded_rose.add_item(new_item)
        self.assertEqual(gilded_rose.items[1], new_item)

    # Additional failed tests implemented below:

    # test logical error with invalid starting quality over 50
    # for backstage passes should raise error
    def test_out_of_bounds_starting_quality_over(self):
        with self.assertRaises(ValueError):
            items = [BackstagePasses("Backstage passes", 1, 60)]
            items.quality()

    # test error (incorrect naming) for backstage pass with <=10 sell
    # in days should increase quality by 2
    def test_backstage_pass_should_increase_quality_sell_in_leq_10(self):
        items = [BackstagePasses("Backstage passes", 8, 30)]
        backstage_pass_item = items[0]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(32, backstage_pass_item.quality)

    # test error (incorrect naming) for backstage pass with <=3 sell
    # in days should increase quality by 3
    def test_backstage_pass_should_increase_quality_sell_in_leq_5(self):
        items = [BackstagePasses("Backstage passes", 3, 30)]
        backstage_pass_item = items[0]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(33, backstage_pass_item.quality)

    # test error for backstage pass (incorrect naming) quality should
    # be 0 after concert date
    def test_backstage_pass_quality_drop_zero_after_concert_date(self):
        items = [BackstagePasses("Backstage passes", -1, 50)]
        backstage_pass_item = items[0]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, backstage_pass_item.quality)


if __name__ == '__main__':
    unittest.main()
