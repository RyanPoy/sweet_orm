#coding: utf8
from collections import OrderedDict as oDict
from sweet_orm.utils.inflection import *
from sweet_orm.utils import import_object, Q


relation_q = Q()


class Relation:

    def delete_all_real_value(self, owner_objs):
        pass

    def set_owner(self, owner):
        self.owner = owner
        self.owner._register_relation(self.name, self)
        return self

    @property
    def target(self):
        """ return target class
        """
        if isinstance(self._target_cls_or_target_name, str):
            self._target_cls_or_target_name = import_object(self._target_cls_or_target_name)
        return self._target_cls_or_target_name

    @property
    def target_name(self):
        if not hasattr(self, '_target_name'):
            if isinstance(self._target_cls_or_target_name, str):
                self._target_name = self._target_cls_or_target_name.split('.')[-1]
            else:
                self._target_name = self._target_cls_or_target_name.__name__
        return self._target_name
