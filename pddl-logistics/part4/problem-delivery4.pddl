(define (problem example1)
  (:domain logistics)
  (:objects
   city1 city2                ;; there are two cities in the example world,
   truck1 truck2              ;; there are two trucks,
   office1 office2 office3    ;; there are three offices,
   packet1                    ;; and the one package that is to be delivered
   packet2                    ;; :)
   PlanEx-building
   Scooty-Puff moppe
   airplane1 airplane2
   airport_city1 airport_city2
   
   )

  (:init
   ;; Declare that packet1 is of type 'object'
   (object packet1)
   (object packet2)
   (large_object packet1)
   (small_object packet2)

   ;; all trucks must be declared as both 'vehicle' and as the specific type of vehicle 'truck'
   (vehicle truck1) (vehicle truck2) (vehicle Scooty-Puff) (vehicle moppe)
   (truck truck1) (truck truck2) (moped Scooty-Puff) (moped moppe)
   (drivable truck1) (drivable truck2)
   (drivable Scooty-Puff) (drivable moppe)
   (vehicle airplane1) (vehicle airplane2) 
   (airplane airplane1) (airplane airplane2)

   ;; we declare that offices are of type 'location' so that trucks can drive to them
   (location office1) (location office2) 
   (location office3) (location PlanEx-building)
   (location airport_city1) (location airport_city2)
   (airport airport_city1) (airport airport_city2)

   ;; likewise, the cities must be declared as 'city'
   (city city1) (city city2) 

   ;; we use 'loc' to say that office1 and office2 are located in city1, while office3 is located in city2
   (loc office1 city1) (loc office2 city1)
   (loc office3 city2) (loc PlanEx-building city1)
   (loc airport_city1 city1) (loc airport_city2 city2)

   ;; we use 'at' to say that packet1 is at office1, truck1 is at office2, and truck2 is at office3
   (at packet1 office1)
   (at packet2 office2)
   (at truck1 office2)
   (at truck2 office3)
   (at Scooty-Puff PlanEx-building)
   (at moppe office3)
   (at airplane1 airport_city1)
   (at airplane2 airport_city2)

   )

  ;; Here we define the goal we want the planner to achieve  
  (:goal (AND (at packet1 office3) (at packet2 office3)))
)

