from django.db import models


class BaseModel(models.Model):
    """
    An abstract base class model that provides self-updating 'created_at' and 'updated_at' fields.

    Attributes:
        created_at (DateTimeField): A timestamp indicating when the object was created.
                                    Automatically set on object creation.
        updated_at (DateTimeField): A timestamp indicating when the object was last updated.
                                    Automatically updated on each save.

    Meta:
        abstract (bool): Indicates that this model should not be used to create any database table.
                            Instead, it should be used as a base class for other models.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        abstract = True
