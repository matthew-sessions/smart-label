from movable_objects import SQ

class BoundingObjectCache:
    def __init__(self):
        self.current_sq_holder = {}
        self.cached_changes = {}
        self.not_yet_saved = {}

    def remove_box(self, id: str):
        if id in self.current_sq_holder:
            sq = self.current_sq_holder[id]
            if (self.cached_changes.get(sq.index, {}) or {}).get(id):
                del self.cached_changes[sq.index][id]
                del self.not_yet_saved[id]
            self.current_sq_holder[id].delete()
            del self.current_sq_holder[id]

    def add_box(self, box: SQ):
        self.current_sq_holder[box.id] = box
        if box.index not in self.cached_changes:
            self.cached_changes[box.index] = {}
        self.cached_changes[box.index][box.id] = box.cv_cords
        self.not_yet_saved[box.id] = box.cv_cords

    def get_all_boxes_from_index(self, index: int):
        boxes = self.cached_changes.get(index, {}) or {}
        return boxes

    def get_box(self, id: str):
        return self.current_sq_holder[id]

    def clear_sq(self):
        for sq in self.current_sq_holder.values():
            sq.delete()
        self.current_sq_holder.clear()

    def update(self, index, id, locinfo):
        if index not in self.cached_changes:
            self.cached_changes[index] = {}
        self.cached_changes[index][id] = locinfo
        self.not_yet_saved[id] = locinfo

    def add_sq_box_only(self, sq):
        self.current_sq_holder[sq.id] = sq
