import pandas as pd
import plotly.express as px
from shiny.express import ui, input
from shinyswatch import theme
from shiny import render
from shinywidgets import render_plotly
from shiny import reactive

df= pd.read_csv('Iris.csv')
print(df.sample)

#add a theme page
ui.page_opts(theme=theme.minty)

# get unique values for species
species = list(df['Species'].unique())

# add a sidebar
with ui.sidebar(title='Parameters'):
    ui.input_selectize(id='species_id',
                       label='Species',
                       choices=species)

ui.panel_title(title='Iris Dashboard' )

#subset dataset
@reactive.calc
def filter_df():
    df_species = df[df['Species'] == input.species_id()]
    return df_species

with ui.card():
    @render_plotly
    def show_scatter():
        plot = px.scatter(data_frame=filter_df(),
                      x='SepalLengthCm', y='SepalWidthCm', size= 'PetalLengthCm',
                          template='ggplot2',
                  title= 'Plot of sepal length VS sepal width')
        return plot

with ui.card():
    with ui.layout_columns(col_widths=[3,3,3,3]):
        @render_plotly
        def show_hist():
            plot = px.histogram(data_frame=filter_df(),
                                x='SepalLengthCm',
                                template='ggplot2',
                                title= 'Sepal length Distribution')
            return plot


        @render_plotly
        def show_hist2():
            plot = px.histogram(data_frame=filter_df(),
                                x='SepalWidthCm',
                                template='ggplot2',
                                title='Sepal width Distribution')
            return plot


        @render_plotly
        def show_hist3():
            plot = px.histogram(data_frame=filter_df(),
                                x='PetalLengthCm',
                                template='ggplot2',
                                title='Petal Length Distribution')
            return plot


        @render_plotly
        def show_hist4():
            plot = px.histogram(data_frame=filter_df(),
                                x='PetalWidthCm',
                                template='ggplot2',
                                title='Petal Width Distribution')
            return plot