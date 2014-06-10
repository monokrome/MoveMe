from rest_framework import serializers


class TreeTextField(serializers.Field):
    def field_to_native(self, obj, name):
        return obj.text


class TreeAttrField(serializers.Field):
    def __init__(self, tree_attr=None, *args, **kwargs):
        if tree_attr:
            self.tree_attr = tree_attr

        super(TreeAttrField, self).__init__(*args, **kwargs)

    def field_to_native(self, obj, name):
        tree_attr = getattr(self, 'tree_attr', name)
        return obj.attrs.get(tree_attr)



