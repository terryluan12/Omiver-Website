from django_components import Component, register

@register("ibutton")
class Icon(Component):
    template_file = "ibutton.html"
    css_file = "ibutton.css"

    def get_template_data(self, args, kwargs, slots, context):
        return kwargs
