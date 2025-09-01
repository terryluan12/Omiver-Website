from django_components import Component, register

@register("setting_item")
class Icon(Component):
    template_file = "setting_item.html"
    css_file = "setting_item.css"

    def get_template_data(self, args, kwargs, slots, context):
        return {
            "title": kwargs["title"],
            "value": kwargs["value"],
            "img_src": kwargs["img_src"],
            "proceed_icon": kwargs["proceed_icon"]
        }