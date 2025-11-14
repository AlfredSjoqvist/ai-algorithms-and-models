
;; This is a plain STRIPS formulation of the standard Logistics domain.

;; Types are defined by static (in the sense that
;; there are no operators that change their truth value) unary predicates.
;; The types of objects in a problem instance must be defined by including
;; the appropriate typing predicates in the initial state. The binary 
;; static predicate "loc" describes the topology of the problem instance: 
;; "(loc ?l ?c)" is true if the location ?l is in city ?c.

(define (domain logistics)
  (:requirements :strips)
  (:predicates
  
   ;; ##### PREDICATES #####

   ;; Static predicates: 
   (object ?o) (truck ?t) (moped ?m) (vehicle ?v) 
   (location ?l) (city ?c) (loc ?l ?c) 

   ;; Non-static predicates:
   (at ?x ?l) ;; ?x (package or vehicle) is at location ?l
   (in ?p ?v) ;; package ?p is in vehicle ?v

   )

  ;; ##### ACTIONS #####

  ;; Load an object into a vehicle.
  (:action load
    :parameters (?o ?v ?l)
    :precondition (and (object ?o) (vehicle ?v) (location ?l)
		       (at ?v ?l) (at ?o ?l))
    :effect (and (in ?o ?v) (not (at ?o ?l))))

  ;; Unload an object from a vehicle.
  (:action unload
    :parameters (?o ?v ?l)
    :precondition (and (object ?o) (vehicle ?v) (location ?l)
		       (at ?v ?l) (in ?o ?v))
    :effect (and (at ?o ?l) (not (in ?o ?v))))

  ;; Drive a vehicle between two locations in the same city.
  (:action drive
    :parameters (?v ?l1 ?l2 ?c)
    :precondition (and (vehicle ?v) (location ?l1) (location ?l2) (city ?c)
		       (at ?v ?l1) (loc ?l1 ?c) (loc ?l2 ?c))
    :effect (and (at ?v ?l2) (not (at ?v ?l1))))

)
