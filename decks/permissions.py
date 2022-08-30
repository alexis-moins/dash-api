from rest_framework import permissions


class IsDeckOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, _, deck) -> bool:
        """
        Return true whether the owner of a deck is the author of the
        request (based on the token).
        """
        # Instance must have an attribute named `owner`.
        return deck.owner == request.user
