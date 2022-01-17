import time
from behave import *
from bdd.pages.catmandu.Hotel_Result_Page import hotel_result_page
from bdd.pages.catmandu.Passenger_page import Passenger_page


@Given("Hacer búsqueda de hoteles en catmandu para ocupación {occupancy:w} para destino iata {destination:w}"
       " con fecha de checkin en {check_future_days:d} días y checkout en {check_out_future_days:d} días")
def step_impl(context, occupancy, destination, check_future_days, check_out_future_days):

    page = hotel_result_page(context)
    page.search_hotel(city=destination, check_future_days=check_future_days, check_out_future_days=check_out_future_days
                      , occupancy=occupancy)
    context.current_page = page


@Then("Esperar que la página de resultados traiga hoteles en catmandú")
def step_impl(context):
    context.current_page.wait_results_hotel()


@Then("Seleccionar la primera opción de hotel")
def step_impl(context):
    context.current_page.click_option_hotel()

@Then("Seleccionar la opción {roomOption:d} del hotel {hotelOption:d} de la página de resultados de catmandú")
def step_impl(context,hotelOption, roomOption):

    if hotelOption >= 1:
        hotelOption = hotelOption-1
    if roomOption >= 1:
        roomOption = roomOption-1

    page = hotel_result_page(context)
    page.click_hotel_option_dinamic(hotelOption, roomOption)


@Then("Esperar la página de pasajeros")
def step_impl(context):
    context.currentPage = Passenger_page(context)
    context.currentPage.wait_for_passenger_page()

@Then("Esperar la validación de precios en página de pasajeros de catmandú")
def step_impl(context):
    context.currentPage.wait_until_price_validation()

@Then("Llenar formulario de pasajeros")
def step_impl(context):
    context.currentPage.fill_passenger_information()

@Then("Click botón continuar en página de pasajeros")
def step_impl(context):
    context.currentPage.click_button_continue()