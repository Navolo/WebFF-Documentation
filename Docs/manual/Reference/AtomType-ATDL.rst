.. _AtomType-ATDL:

Atom Type - ATDL
================

XML Schema
----------

The XML schema for the **Atom Type - ATDL** has the following representation (design mode representation using Liquid XML Studio):

.. image:: ../../images/AtomType-ATDL.png
	:align: left

The general attributes (describing the entire set of atoms) are given by:

====================== =============== =======================================
**General Attributes** **Cardinality** **Value/Definition**               
---------------------- --------------- ---------------------------------------
Nomenclature           Fixed           ATDL
comment                Optional        Comment attached to set of atoms
====================== =============== =======================================

The specific attributes (attached to each atom description) are given by:

======================= =============== =======================================
**Specific Attributes** **Cardinality** **Value/Definition**               
----------------------- --------------- ---------------------------------------
Description             Required        Description of the atom
Element                 Required        Corresponding element of the atom
AtomicNumber            Required        Corresponding atomic number of the atom
AtomicMass              Required        Corresponding atomic mass of the atom
======================= =============== =======================================

The specific elements (contained within each instance of the atom template) are given by:

======================= =============== =======================================
**Specific Elements**   **Cardinality** **Value/Definition**               
----------------------- --------------- ---------------------------------------
AtomType-Name           Required        Atom type name
Atom                    Required        Atom
BondedAtoms             Required        Bonded atoms
FormalCharge            Optional        Formal charge of the atom
======================= =============== =======================================

Note that an XML document will be rejected from being entered into the WebFF database if a required attribute is left unspecified.

References
----------

1. `Atom-type description language`_.

2. `Liquid XML Studio`_.

.. _Atom-type description language: https://link.springer.com/article/10.1007/s00214-002-0402-6

.. _Liquid XML Studio: https://www.liquid-technologies.com/