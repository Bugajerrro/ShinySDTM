from shiny import App, ui, run_app


# Creating the UI of the Shiny Application

app_ui = ui.page_navbar(title="Shiny for SDTM", window_title="Shiny for SDTM")


# Run the Shiny App

def server(input, output, session):
     pass

app = App(app_ui, server)

if __name__ == "__main__":
     run_app(reload=True)