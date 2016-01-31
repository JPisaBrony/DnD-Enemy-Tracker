import gtk

class Base:
    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("dnd_tracker_layout.glade")
        self.builder.connect_signals(self)
        
    def main(self):
        self.builder.get_object("window1").show_all()
        self.store = self.builder.get_object("liststore1")
        self.tree = self.builder.get_object("treeview1")
        self.name = self.builder.get_object("entry1")
        self.hp = self.builder.get_object("entry2")
        self.loc = self.builder.get_object("entry3")
        self.edit_name = self.builder.get_object("entry4")
        self.edit_hp = self.builder.get_object("entry5")
        self.edit_loc = self.builder.get_object("entry6")
        gtk.main()
    
    def add_item(self, widget):
        try:
            hp = int(self.hp.get_text())
        except ValueError:
            return
        loc = self.loc.get_text()
        name = self.name.get_text()
        if loc == "":
            return
        if name == "":
            return
        self.store.append([name, hp, loc])
    
    def selected_new(self, widget):
        (model, pathlist) = self.tree.get_selection().get_selected_rows()
        for path in pathlist:
            iter = model.get_iter(path)
            name = model.get_value(iter, 0)
            hp = model.get_value(iter, 1)
            loc = model.get_value(iter, 2)
            self.edit_name.set_text(name)
            self.edit_hp.set_text(str(hp))
            self.edit_loc.set_text(loc)
    
    def update_table(self, widget):
        (model, pathlist) = self.tree.get_selection().get_selected_rows()
        for path in pathlist:
            try:
                hp = int(self.edit_hp.get_text())
            except ValueError:
                return
            loc = self.edit_loc.get_text()
            name = self.edit_name.get_text()
            if loc == "":
                return
            if name == "":
                return
            iter = model.get_iter(path)
            model.set_value(iter, 0, name)
            model.set_value(iter, 1, hp)
            model.set_value(iter, 2, loc)
    
    def sub_one(self, widget):
        self.sub_value(1)
        self.update_hp()

    def sub_five(self, widget):
        self.sub_value(5)
        self.update_hp()

    def sub_ten(self, widget):
        self.sub_value(10)
        self.update_hp()
    
    def sub_value(self, val):
        (model, pathlist) = self.tree.get_selection().get_selected_rows()
        for path in pathlist:
            iter = model.get_iter(path)
            hp = model.get_value(iter, 1)
            model.set_value(iter, 1, hp - val)
    
    def update_hp(self):
        (model, pathlist) = self.tree.get_selection().get_selected_rows()
        for path in pathlist:
            iter = model.get_iter(path)
            hp = model.get_value(iter, 1)
            self.edit_hp.set_text(str(hp))
    
    def delete_row(self, widget):
        (model, pathlist) = self.tree.get_selection().get_selected()
        if pathlist:
            path = model.get_path(pathlist)[0]
            model.remove(pathlist)
    
    def destory(self, widget, data=None):
        gtk.main_quit()
    
if __name__ == "__main__":
    Base().main()