# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashWaffleChart(Component):
    """A DashWaffleChart component.


Keyword arguments:

- id (string; required)

- barHeightName (string; optional)

- colors (list of strings; default ['#FF8E79', '#FF6B5B', '#FF4941', '#DB1D25'])

- data (list of boolean | number | string | dict | lists; required)

- groupName (string; required)

- icon (string; default False)

- style (dict; optional)

    `style` is a dict with keys:

    - barColor (string; optional)

    - barFillColor (string; optional)

    - faceColor (string; optional)

    - labelColor (string; optional)

- valueName (string; required)

- width (number; default 600)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_waffle_chart'
    _type = 'DashWaffleChart'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, width=Component.UNDEFINED, data=Component.REQUIRED, valueName=Component.REQUIRED, barHeightName=Component.UNDEFINED, groupName=Component.REQUIRED, icon=Component.UNDEFINED, colors=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'barHeightName', 'colors', 'data', 'groupName', 'icon', 'style', 'valueName', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'barHeightName', 'colors', 'data', 'groupName', 'icon', 'style', 'valueName', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'data', 'groupName', 'valueName']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashWaffleChart, self).__init__(**args)
