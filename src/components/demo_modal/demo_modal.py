from django_components import Component, register

@register("demo_modal")
class Icon(Component):
    template_file = "demo_modal.html"
    css_file = "demo_modal.css"
    js_file = "demo_modal.js"

    def get_template_data(self, args, kwargs, slots, context):
        return {
        }