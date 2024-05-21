# Функциональные модели

# Функциональные модели

@startuml
left to right direction
actor User as U
rectangle "Театральное приложение" {
    usecase "Просмотр информации о режиссерах" as A
    usecase "Просмотр информации об организаторах" as B
    usecase "Просмотр информации о дизайнерах" as C
    usecase "Просмотр информации о SMM-специалистах" as D
    usecase "Просмотр информации о кураторе актеров" as E
    usecase "Просмотр информации о кураторе командообразования" as F
    U --> (A)
    U --> (B)
    U --> (C)
    U --> (D)
    U --> (E)
    U --> (F)
}
@enduml

@startuml
:User: --> (Start)
:Start: --> (View Directors Info)
if (Is User Logged In?) then (yes)
  -->[yes] (Retrieve Directors Info)
  -->[yes] (Display Directors Info)
else (no)
  -->[no] (Ask User to Log In)
  --> (End)
endif
:Display Directors Info: --> (End)
:End:
@enduml
