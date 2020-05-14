#coding: utf8
from sweet.orm.relations.relation import Relation, relation_q
from sweet.utils.inflection import *
from sweet.utils import *


class HasMany(Relation):
    
    def __init__(self, owner=None, target=None, name=None, fk=None, cascade=False):
        """ owner model has many target model
        :param owner: model class
        :param target: model class
        :param name: attribute name of owner.
        :param fk: foreign key of target
        :param pk: primary key of owner
        eg. User has many Mobile
          owner = User
          target = Mobile
          name = 'mobiles'      # can retrive use User().mobiles
          fk = 'user_id'        # can retrive use Mobile().user_id
        """
        self.owner = owner
        self.cascade = cascade
        self._target_cls_or_target_name = target
        self.name = name
        self._target_fk = fk

    @property
    def target_fk(self):
        """ return target foreign key
        eg. user has many mobiles
            fk equals 'user_id', which composition is ： 'user' + '_'+ user.pk
        """
        if not self._target_fk:
            name = self.owner.__name__.split('.')[-1]
            self._target_fk = '{owner_name}_{owner_pk}'.format(
                owner_name=pythonize(name),
                owner_pk=self.owner.__pk__
            )
        return self._target_fk

    def get_real_value(self, owner_obj):
        """ eg. user has many mobiles
            Mobile.where(user_id=user.id).all()
        """
        return self.target.where(**{self.target_fk: owner_obj.get_pk()})

    def delete_all_real_value(self, owner_objs):
        """ eg. user has many mobiles
            1) User.delete_all() # should be delete all mobiles which belongs to users

            2) u = User.first()
               u.delete()  # should be delete mobiles which belongs to u
        """
        if self.cascade:
            pks = [ o.get_pk() for o in owner_objs ]
            if pks:
                self.target.delete_all(**{self.target_fk: pks})
        return self

    def inject(self, owner_model, target_model):
        attr_name = self.target_fk
        setattr(owner_model, attr_name, target_model.get_pk())


def has_many(name, clazz, fk=None, pk=None, cascade=False):
    r = HasMany(target=clazz, name=name, fk=fk, cascade=cascade)
    relation_q.put(r)

