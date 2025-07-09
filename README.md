This is a Booking API .
Total of 3 apis are there,
EndPoints: 
  GET /classes
    endpoint_url - {{base_url}}/classes
    response - {
                "status": true,
                "classes": [
                    {
                        "id": 1,
                        "date": "2025-07-11",
                        "master_class__class_name": "Yoga",
                        "instructor__name": "Rahul Bal",
                        "total_slots": 12,
                        "available_slots": 10
                    },
                    {
                        "id": 2,
                        "date": "2025-07-19",
                        "master_class__class_name": "HIIT",
                        "instructor__name": "Shalini Menon",
                        "total_slots": 26,
                        "available_slots": 26
                    }
                ]
            }
    Returns a list of all upcoming fitness classes (name, date/time, instructor, available slots)
  POST /book
    endpoint - {{base_url}}/bookings?email=abc@gmail.com
    payload - {"class_id": 1, "client_name": "rahul", "client_email": "abc@gmail.com"}
    Accepts a booking request (class_id, client_name, client_email)
  GET /bookings
    endpoint - {{base_url}}/bookings?email=abc@gmail.com
    response - {
                  "status": true,
                  "classes": [
                      {
                          "regular_class__date": "2025-07-11",
                          "client__name": "Giri narayan",
                          "regular_class__instructor__name": "Rahul Bal",
                          "regular_class__master_class__class_name": "Yoga"
                      },
                      {
                          "regular_class__date": "2025-07-11",
                          "client__name": "Giri narayan",
                          "regular_class__instructor__name": "Rahul Bal",
                          "regular_class__master_class__class_name": "Yoga"
                      },
                      {
                          "regular_class__date": "2025-07-11",
                          "client__name": "Giri narayan",
                          "regular_class__instructor__name": "Rahul Bal",
                          "regular_class__master_class__class_name": "Yoga"
                      }
                  ]
              }
    Returns all bookings made by a specific email address
