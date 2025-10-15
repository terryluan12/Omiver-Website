from django_components import Component, register

@register("custom_slider")
class CustomSlider(Component):
    template_file = "custom_slider.html"
    css_file = "custom_slider.css"

    def get_template_data(self, args, kwargs, slots, context):
        return {
            "marker": kwargs.get("marker", "Marker"),
            "value": kwargs.get("value", 0),
            "min": kwargs.get("min", 0),
            "max": kwargs.get("max", 100),
        }