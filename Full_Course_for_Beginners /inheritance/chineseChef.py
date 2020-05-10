from chef import Chef

# intro = "The chef makes "


class ChineseChef(Chef):

    def make_special_dish(self):
        print(intro + "orange chicken")

    def make_fried_rice(self):
        print(intro + "fried rice")