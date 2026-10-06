# Hotel Reservation Management System

A modular Python-based Hotel Reservation Management System for
managing guests, rooms, reservations, payments, and hotel reports.

## Features

### Guest Management

- Add guests
- View guests
- Search guests
- Delete guests

### Room Management

- Add rooms
- View rooms
- Search rooms
- View available rooms
- Track room status

### Reservation Management

- Create reservations
- Prevent double booking
- Calculate number of nights
- Calculate room charges
- Add extra charges
- Calculate GST
- Calculate grand total
- Check-in guests
- Check-out guests
- Cancel reservations
- Search reservations
- View reservation details

### Payment Management

- Record payments
- View payment history
- Check pending balance
- Prevent overpayment

### Reports

- Total rooms
- Available rooms
- Reserved rooms
- Occupied rooms
- Total reservations
- Collected revenue
- Reservation status report

## Technologies

- Python
- JSON
- File Handling
- Datetime
- Functions
- Modular Programming

## Project Structure

hotel-reservation-management/
│
├── main.py
├── config.py
├── storage.py
├── utils.py
├── guest_manager.py
├── room_manager.py
├── reservation_manager.py
├── payment_manager.py
├── report_manager.py
│
├── data/
│   ├── guests.json
│   ├── rooms.json
│   ├── reservations.json
│   └── payments.json
│
└── README.md

## How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/hotel-reservation-management.git
