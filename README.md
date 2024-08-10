# Sally's Flower Shop - Odoo 16 Module

## Overview

The **Sally's Flower Shop** module is designed to manage a flower shop's operations, including product management, sales, stock tracking, and weather integration. The module adds functionality to track flowers, manage their watering schedules, and integrate weather data to optimize watering times.

## Features

- **Flower Management**: Define flowers with their common and scientific names, seasons, and watering needs.
- **Product Integration**: Link flower records with products to manage inventory and sales.
- **Watering Log**: Maintain a history of watering activities, linked to specific flower lots.
- **Weather Integration**: Fetch real-time weather data to adjust watering schedules based on current conditions.
- **Custom Reports**: Generate detailed sales reports for flower orders.

## Installation

1. Copy the `sally_flower_shop` directory into your Odoo `addons` directory.
2. Update your Odoo app list by going to **Apps** > **Update Apps List**.
3. Search for **Sally Flower Shop** and install the module.

## Dependencies

This module depends on the following Odoo modules:

- `base`
- `product`
- `sale`
- `website_sale`
- `stock`

## Usage

### Flower Management

- Navigate to **Flowers** under the **Sales** menu.
- Create new flower records, specifying details like watering frequency and season.

### Watering Logs

- Watering activities are automatically logged based on the flower's watering frequency and weather conditions.
- Manually create logs or review existing logs by navigating to **Watering Logs** under the **Inventory** menu.

### Weather Integration

- Ensure that your warehouse location has valid latitude and longitude coordinates.
- The module uses the OpenWeather API to fetch weather data. Configure your API key in **Settings** > **Technical** > **System Parameters**.

### Reports

- Generate flower sales reports by navigating to **Sales** > **Reports** > **Flower Sales Report**.
- Use the "Print Flower Report" button on the sales order form to generate a detailed report for a specific order.

## Configuration

### Weather API Key

To set up the weather integration:

1. Go to **Settings** > **Technical** > **System Parameters**.
2. Create a new parameter with the key `flower_shop.weather_api_key` and enter your OpenWeather API key as the value.
