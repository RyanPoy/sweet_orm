# coding: utf8
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from tests.__init__ import TestCase
import unittest
import os
from template import Template


class PasswordFieldTest(TestCase):

    def test_form_with_url_and_password_field(self):
        t = Template("""
<%= using form(url="/user/new") do f %>
    <%= f.password_field('pass') %>
<% end %>
""")
        self.assertEqual("""
<form action="/user/new" method="GET" accept-charset="UTF8">
    <input id="pass" name="pass" type="password" />
</form>
""", t.render())

        t = Template("""
<%= using form(url="/user/new") do f %>
    <%= f.password_field('secret', 'Your secret here') %>
<% end %>
""")
        self.assertEqual("""
<form action="/user/new" method="GET" accept-charset="UTF8">
    <input id="secret" name="secret" type="password" value="Your secret here" />
</form>
""", t.render())

        t = Template("""
<%= using form(url="/user/new") do f %>
    <%= f.password_field('masked', _class='masked_input_field') %>
<% end %>
""")
        self.assertEqual("""
<form action="/user/new" method="GET" accept-charset="UTF8">
    <input id="masked" name="masked" type="password" class="masked_input_field" />
</form>
""", t.render())

        t = Template("""
<%= using form(url="/user/new") do f %>
    <%= f.password_field('token', '', size=15) %>
<% end %>
""")
        self.assertEqual("""
<form action="/user/new" method="GET" accept-charset="UTF8">
    <input id="token" name="token" type="password" value="" size="15" />
</form>
""", t.render())

        t = Template("""
<%= using form(url="/user/new") do f %>
    <%= f.password_field('key', maxlength=16) %>
<% end %>
""")
        self.assertEqual("""
<form action="/user/new" method="GET" accept-charset="UTF8">
    <input id="key" name="key" type="password" maxlength="16" />
</form>
""", t.render())

        t = Template("""
<%= using form(url="/user/new") do f %>
    <%= f.password_field('confirm_pass', disabled=True) %>
<% end %>
""")
        self.assertEqual("""
<form action="/user/new" method="GET" accept-charset="UTF8">
    <input id="confirm_pass" name="confirm_pass" type="password" disabled="disabled" />
</form>
""", t.render())

        t = Template("""
<%= using form(url="/user/new") do f %>
    <%= f.password_field('pin', '1234', maxlength=4, size=6, _class="pin_input") %>
<% end %>
""")
        self.assertEqual("""
<form action="/user/new" method="GET" accept-charset="UTF8">
    <input id="pin" name="pin" type="password" value="1234" size="6" maxlength="4" class="pin_input" />
</form>
""", t.render())


if __name__ == '__main__':
    unittest.main()
