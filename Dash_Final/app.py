#libraries
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
import os
#from callbacks import register_callbacks
    
# Dash instance declaration
app = dash.Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.MINTY],)


#Top menu, items get from all pages registered with plugin.pages
navbar = dbc.NavbarSimple([

    dbc.NavItem(dbc.NavLink("Home", href="/")),
    ##
    dbc.NavItem(dbc.NavLink("Disposed waste", href="/waste_disposed")),
    dbc.NavItem(dbc.NavLink("Effectively used", href="/waste_effectively_used")),
    dbc.NavItem(dbc.NavLink("Model", href="/Model")),
    ],
    brand="DS4A Project - Team 207",
    color="primary",
    dark=True,
    className="mb-2",
)

#Main layout
app.layout = dbc.Container(
    [
        navbar,
        dl.plugins.page_container,
    ],
    className="dbc",
    fluid=True,
)

# Call to external function to register all callbacks
#register_callbacks(app)


# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050, proxy=None, debug=True)