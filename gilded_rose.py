# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class SubItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        pass


class NormalItem(SubItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.sell_in >= 0 and self.quality > 1:
            self.quality -= 1
        elif self.sell_in < 0 and self.quality > 2:
            self.quality -= 2
        else:
            self.quality = 0
        self.sell_in -= 1


class AgedBrie(SubItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1


class Sulfuras(SubItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.sell_in -= 1


class BackstagePasses(SubItem):
    def __init__(self, name, sell_in, quality):
        if quality < 0 or quality > 50:
            raise ValueError("Quality must be between 0 and 50")
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in <= 5:
            if self.quality > 47 and self.quality <= 50:
                self.quality = 50
            elif self.quality <= 47:
                self.quality += 3
        elif self.sell_in <= 10:
            if self.quality == 49 or self.quality == 50:
                self.quality = 50
            elif self.quality <= 48:
                self.quality += 2


class Conjured(SubItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.sell_in >= 0 and self.quality > 2:
            self.quality -= 2
        elif self.sell_in < 0 and self.quality > 4:
            self.quality -= 4
        else:
            self.quality = 0
        self.sell_in -= 1


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for i in self.items:
            i.update_quality()

    def get_items(self):
        return self.items

    def add_item(self, SubItem):
        self.items.append(SubItem)
