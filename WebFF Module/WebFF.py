''' This modual contains functions that translate data between excel, XMl, and molecular dynamics text formats
'''
import xml.etree.ElementTree as ET 		  # Python standard library	
import xlrd                               # NEEDs to be installed

#function below beginging with ReadExcel read in indivual sheet from the webff excel template and transleate them into XML that fits the webff XML schema
def ReadExcelMetaData_Header(sheet, sub_root): 
    ''' Reads in the MetaData sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    
    field1 = ET.SubElement(sub_root, "Force-Field-Protocol").text = xls_sheet.row_values(4)[1]
    field2 = ET.SubElement(sub_root, "Force-Field-Name").text = xls_sheet.row_values(5)[1]
    field1 = ET.SubElement(sub_root, "Description").text = xls_sheet.row_values(6)[1]
    field3 = ET.SubElement(sub_root, "Data-Source")
    field4 = ET.SubElement(field3, "Compact")
    field1 = ET.SubElement(field4, "Reference").text = xls_sheet.row_values(7)[1]
    field2 = ET.SubElement(field4, "DOI").text = xls_sheet.row_values(8)[1]
    field1 = ET.SubElement(field4, "URL").text = xls_sheet.row_values(9)[1]
    field2 = ET.SubElement(field4, "Notes").text = xls_sheet.row_values(10)[1]
    field4 = ET.SubElement(sub_root, "Data-Source-Scribe")
    field1 = ET.SubElement(field4, "Name").text = xls_sheet.row_values(11)[1]
    field1 = ET.SubElement(field4, "Affiliation").text = xls_sheet.row_values(12)[1]
    field2 = ET.SubElement(field4, "email").text = xls_sheet.row_values(13)[1]

def ReadExcelMetaData_Keywords(sheet, root): 
    ''' Reads in the Keywords sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    sub_root = root.find("./Force-Field-Header")

    # Row 2 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(4))

    for col_num in xrange(0, xls_sheet.ncols):
        for row_num , cell_value in enumerate(xls_sheet.col_values(col_num)[5:]):
            if (len(str(cell_value))!=0 and str(cell_value) != "?") :
                ET.SubElement(sub_root, xls_sheet_header[col_num]).text = str(cell_value)
    
def ReadExcelBondPotential_Harmonic(sheet, sub_root): 
    ''' Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "BondPotential-Harmonic", {'style':AA, 'formula':BB, 'K-units':CC, 'R0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Bond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelBondPotential_Quartic(sheet, sub_root): 
    ''' Reads in the BondPotential-Quartic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "BondPotential-Quartic", {'style':AA, 'formula':BB, 'K-units':CC, 'R0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Bond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelBondPotential_Morse(sheet, sub_root): 
    ''' Reads in the BondPotential-Morse sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "BondPotential-Morse", {'style':AA, 'formula':BB, 'D-units':CC, 'A-units':DD, 'R0-units':EE})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))
    for row_num in xrange(9, xls_sheet.nrows):

        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Bond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
def ReadExcelAnglePotential_Harmonic(sheet, sub_root): 
    ''' Reads in the AnglePotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "AnglePotential-Harmonic", {'style':AA, 'formula':BB, 'Ka-units':CC, 'Theta0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("precedence")
        attribute_idx2 = xls_sheet_header.index("comment")
        attribute_idx3 = xls_sheet_header.index("version")
        attribute_idx4 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Angle")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'precedence', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx4])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == attribute_idx4: 
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 

def ReadExcelAnglePotential_COS2(sheet, sub_root): 
    ''' Reads in the AnglePotential-COS2 sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "AnglePotential-COS2", {'style':AA, 'formula':BB, 'Ka-units':CC, 'Theta0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("precedence")
        attribute_idx2 = xls_sheet_header.index("comment")
        attribute_idx3 = xls_sheet_header.index("version")
        attribute_idx4 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Angle")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'precedence', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx4])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == attribute_idx4: 
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 

def ReadExcelAnglePotential_CHARMM(sheet, sub_root): 
    ''' Reads in the AnglePotential-CHARMM sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet
    
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]
    FF=xls_sheet.row_values(7)[1]

    sheet = ET.SubElement(sub_root, "AnglePotential-CHARMM", {'style':AA, 'formula':BB, 'Ka-units':CC, 'Theta0-units':DD, 'Kub-units':EE, 
                                                           'Rub-units':FF})

    # Row 9 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(9))

    for row_num in xrange(10, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("precedence")
        attribute_idx2 = xls_sheet_header.index("comment")
        attribute_idx3 = xls_sheet_header.index("version")
        attribute_idx4 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Angle")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'precedence', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx4])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == attribute_idx4: 
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelDihedralPotential_CHARMM(sheet, sub_root): 
    ''' Reads in the DihedralPotential-CHARMM sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-CHARMM", {'style':AA, 'formula':BB, 'convention':CC, 'Kd-units':DD, 'Phi0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
	attribute_idx1 = xls_sheet_header.index("comment")
	attribute_idx2 = xls_sheet_header.index("version")
	attribute_idx3 = xls_sheet_header.index("reference")
	force_integer_idx1 = xls_sheet_header.index("N")
	cur_entry = ET.SubElement(sheet, "Dihedral")
	if (xls_sheet.cell_value(row_num, attribute_idx1)) :
	    ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
	if (xls_sheet.cell_value(row_num, attribute_idx2)) :
	    ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
	if (xls_sheet.cell_value(row_num, attribute_idx3)) :
	    ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
	for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
	    if (len(str(cell_value))!=0) :
		if col_num == attribute_idx1:
		    continue
		elif col_num == attribute_idx2:
		    continue
		elif col_num == attribute_idx3:
		    continue
		elif col_num == force_integer_idx1:
		    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		else:
		    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelDihedralPotential_Harmonic(sheet,sub_root): 
    ''' Reads in the DihedralPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-Harmonic", {'style':AA, 'formula':BB, 'convention':CC, 'Kd-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
	force_integer_idx1 = xls_sheet_header.index("Ns")
	force_integer_idx2 = xls_sheet_header.index("N")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
		elif col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		elif col_num == force_integer_idx2:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		else:
		    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelDihedralPotential_Quadratic(sheet, sub_root): 
    ''' Reads in the DihedralPotential-Quadratic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-Quadratic", {'style':AA, 'formula':BB, 'convention':CC, 'Kd-units':DD, 'Phi0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelDihedralPotential_OPLS(sheet, sub_root): 
    ''' Reads in the DihedralPotential-OPLS sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-OPLS", {'style':AA, 'formula':BB, 'convention':CC, 'Kn-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelDihedralPotential_FourierSimple(sheet, sub_root): 
    ''' Reads in the DihedralPotential-FourierSimple sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-FourierSimple", {'style':AA, 'formula':BB, 'convention':CC, 'Kn-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 

def ReadExcelDihedralPotential_Fourier(sheet, sub_root): 
    ''' Reads in the DihedralPotential-Fourier sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-Fourier", {'style':AA, 'formula':BB, 'convention':CC, 'Kn-units':DD, 'Dn-units':EE})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
	force_integer_idx1 = xls_sheet_header.index("N1")
	force_integer_idx2 = xls_sheet_header.index("N2")
	force_integer_idx3 = xls_sheet_header.index("N3")
	force_integer_idx4 = xls_sheet_header.index("N4")
	force_integer_idx5 = xls_sheet_header.index("N5")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
		elif col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		elif col_num == force_integer_idx2:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		elif col_num == force_integer_idx3:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		elif col_num == force_integer_idx4:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		elif col_num == force_integer_idx5:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		else:
		    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
            
def ReadExcelImproperPotential_CVFF(sheet, sub_root): 
    ''' Reads in the ImproperPotential-CVFF sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-CVFF", {'style':AA, 'formula':BB, 'convention':CC, 'Ki-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
	force_integer_idx1 = xls_sheet_header.index("Ns")
	force_integer_idx2 = xls_sheet_header.index("N")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
		elif col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		elif col_num == force_integer_idx2:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		else:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelImproperPotential_COS2(sheet, sub_root): 
    ''' Reads in the ImporperPotential-COS2 sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-COS2", {'style':AA, 'formula':BB, 'convention':CC, 'Ki-units':DD, 'Chi0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
def ReadExcelImproperPotential_Harmonic(sheet, sub_root): 
    ''' Reads in the ImporperPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-Harmonic", {'style':AA, 'formula':BB, 'convention':CC, 'Ki-units':DD, 'Chi0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelImproperPotential_Fourier(sheet, sub_root): 
    ''' Reads in the ImporperPotential-Fourier sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-Fourier", {'style':AA, 'formula':BB, 'convention':CC, 'Ki-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 

def ReadExcelImproperPotential_Umbrella(sheet, sub_root): 
    ''' Reads in the ImporperPotential-Umbrella sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-Umbrella", {'style':AA, 'formula':BB, 'convention':CC, 'Ki-units':DD, 'w0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 

def ReadExcelImproperPotential_CHARMM(sheet, sub_root): 
    ''' Reads in the ImporperPotential-CHARMM sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-CHARMM", {'style':AA, 'formula':BB, 'convention':CC, 'Kd-units':DD, 'Phi0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
	force_integer_idx1 = xls_sheet_header.index("N")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
		elif col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		else:
		    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelNonBondPotential_LJ(sheet, sub_root): 
    ''' Reads in the NonBondPotential-LJ sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'sigma-units':DD, 'Combining-Rule':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
def ReadExcelNonBondPotential_LJRmin(sheet, sub_root): 
    ''' Reads in the NonBondPotential-LJRmin sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ-Rmin", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'Rmin-units':DD, 'Combining-Rule':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 

def ReadExcelNonBondPotential_LJAB(sheet, sub_root): 
    ''' Reads in the NonBondPotential-LJAB sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ-AB", {'style':AA, 'formula':BB, 'A-units':CC, 'B-units':DD, 'Combining-Rule':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelNonBondPotential_LJ96 (sheet, sub_root): 
    ''' Reads in the NonBondPotential-LJRmin sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ96", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'sigma-units':DD, 'Combining-Rule':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
			if col_num == attribute_idx1:
				continue 
			elif col_num == attribute_idx2:
				continue
			elif col_num == attribute_idx3:
				continue 
			ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelNonBondPotential_LJ2(sheet, sub_root): 
    ''' Reads in the NonBondPotential-LJ2 sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    ''' 
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ2", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'sigma-units':DD, 'Combining-Rule':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelEquivalenceTable(sheet, sub_root): 
    ''' Reads in the Equivalence-Table sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    # Row 4 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(4))

    for row_num in xrange(5, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sub_root, "Equivalence")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)   

def ReadExcelAutoEquivalenceTable(sheet, sub_root): 
    ''' Reads in the Equivalence-Table sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    # Row 4 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(4))

    for row_num in xrange(5, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sub_root, "AutoEquivalence")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)  

def ReadExcelBondIncrements(sheet, sub_root): 
    ''' Reads in the Bond-Increments sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    # Row 4 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(4))

    for row_num in xrange(5, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sub_root, "BondIncrement")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelAtomTypes(sheet,root): 
    ''' Reads in the Atom-Types sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]

    sheet = ET.SubElement(root, "AtomTypes", {'PatternNomenclatureStyle':AA, 'comment':BB}) 
    # Row 5 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(5))

    for row_num in xrange(6, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("Element")
        attribute_idx2 = xls_sheet_header.index("AtomicNumber")
        attribute_idx3 = xls_sheet_header.index("AtomicMass")
        attribute_idx4 = xls_sheet_header.index("Description")
        cur_entry = ET.SubElement(sheet, "AtomType")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'Element', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'AtomicNumber', str(int((xls_sheet.row_values(row_num)[attribute_idx2]))))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'AtomicMass', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'Description', str((xls_sheet.row_values(row_num)[attribute_idx4])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == attribute_idx4:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelAtomTypeAttributes(sheet,root): 
    ''' Reads in the Atom-Types-Attributes sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet1 = sheet

    # Row 4 is the header
    xls_sheet1_header = map(str, xls_sheet1.row_values(4))
    for row_num in xrange(5, xls_sheet1.nrows):
        attribute_idx1 = xls_sheet1_header.index("AtomType-Name")
        for child in root.findall("./AtomTypes/AtomType"): 
            AtomTypeName = (child.find("AtomType-Name"))
            if(AtomTypeName.text == str(xls_sheet1.cell_value(row_num, 0))): 
                sheet1 = ET.SubElement(child, "Atom-Attributes")
                sheet2 = ET.SubElement(sheet1, "Attribute")
                for col_num, cell_value in enumerate(xls_sheet1.row_values(row_num)):
                    if (len(str(cell_value))!=0) :
                        if col_num == attribute_idx1:
                            continue    
                        if(type(cell_value) == float): 
                            ET.SubElement(sheet2, xls_sheet1_header[col_num]).text = str(int(cell_value)) 
                        else:
                            ET.SubElement(sheet2, xls_sheet1_header[col_num]).text = str(cell_value) 
                            
                            
#Class2 functions
def ReadExcelBondPotential_Class2(sheet, sub_root): 
    ''' Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "BondPotential-Class2", {'style':AA, 'formula':BB, 'K-units':CC, 'R0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        #cur_entry = ET.SubElement(sheet, "Bond", comment=str((xls_sheet.row_values(row_num)[attribute_idx1])),
        #                          version=str(xls_sheet.row_values(row_num)[attribute_idx2]),
        #                          reference=str(xls_sheet.row_values(row_num)[attribute_idx3]))
	cur_entry = ET.SubElement(sheet, "Bond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    
def ReadExcelAnglePotential_Class2(sheet, sub_root): 
    ''' Reads in the AnglePotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "AnglePotential-Class2", {'style':AA, 'formula':BB, 'K-units':CC, 'Theta0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("precedence")
        attribute_idx2 = xls_sheet_header.index("comment")
        attribute_idx3 = xls_sheet_header.index("version")
        attribute_idx4 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Angle")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'precedence', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx3])))
	if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            elif col_num == attribute_idx4: 
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 

def ReadExcelDihedralPotential_Class2(sheet, sub_root): 
    ''' Reads in the DihedralPotential-CHARMM sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-Class2", {'style':AA, 'formula':BB, 'convention':CC, 'Kn-units':DD, 'Phin-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
          
def ReadExcelImproperPotential_Class2(sheet, sub_root): 
    ''' Reads in the ImporperPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-Class2", {'style':AA, 'formula':BB, 'convention':CC, 'Ki-units':DD, 'Chi0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
			if col_num == attribute_idx1:
				continue 
			elif col_num == attribute_idx2:
				continue
			elif col_num == attribute_idx3:
				continue
			ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
            
def ReadExcelCrossPotential_BondBond(sheet, sub_root): 
    ''' Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-BondBond", {'style':AA, 'formula':BB, 'M-units':CC, 'Ri-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
            
def ReadExcelCrossPotential_BondBond13(sheet, sub_root): 
    ''' Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-BondBond13", {'style':AA, 'formula':BB, 'N-units':CC, 'Ri-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
            
def ReadExcelCrossPotential_AngleAngle(sheet, sub_root): 
    ''' Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-AngleAngle", {'style':AA, 'formula':BB, 'M-units':CC, 'Theta-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
           
def ReadExcelCrossPotential_BondAngle(sheet, sub_root): 
    ''' Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-BondAngle", {'style':AA, 'formula':BB, 'N-units':CC, 'Ri-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
            
def ReadExcelCrossPotential_MiddleBondTorsion(sheet, sub_root): 
    ''' Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-MiddleBondTorsion", {'style':AA, 'formula':BB, 'A-units':CC, 'R-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
            
def ReadExcelCrossPotential_EndBondTorsion(sheet, sub_root): 
    ''' Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-EndBondTorsion", {'style':AA, 'formula':BB, 'B-units':CC, 'C-units':DD, 'R-units':EE})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
            
def ReadExcelCrossPotential_AngleTorsion(sheet, sub_root): 
    ''' Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-AngleTorsion", {'style':AA, 'formula':BB, 'D-units':CC, 'E-units':DD, 'Theta-units':EE})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
            
def ReadExcelCrossPotential_AngleAngleTorsion(sheet, sub_root): 
    ''' Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]


    sheet = ET.SubElement(sub_root, "CrossPotential-AngleAngleTorsion", {'style':AA, 'formula':BB, 'M-units':CC, 'Theta-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
            
def ReadExcelCrossPotential_AngleAngleTorsion(sheet, sub_root): 
    ''' Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]


    sheet = ET.SubElement(sub_root, "CrossPotential-AngleAngleTorsion", {'style':AA, 'formula':BB, 'M-units':CC, 'Theta-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
            
def ReadExcelNonBondPotential_LJClass2(sheet, sub_root): 
    ''' Reads in the NonBondPotential-LJClass2 sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-Class2", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'sigma-units':DD, 'Combining-Rule':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference") 
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

#Coarse grained potentials (Tabular form)

def ReadExcelBondPotential_Tabular(sheet, sub_root): 
    ''' Reads in the BondPotential-Tabular sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    # Handling attributes
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "BondPotential-Tabular", {'style':AA, 'bond-length-units':BB, 'energy-units':CC, 'force-units':DD})

    # Handling comments, version, and reference
    if (xls_sheet.row_values(7)[1]) :
        ET.Element.set(sheet, 'comment', str(xls_sheet.row_values(7)[1]))
    if (xls_sheet.row_values(8)[1]) : 
        ET.Element.set(sheet, 'version', str(xls_sheet.row_values(8)[1]))
    if (xls_sheet.row_values(9)[1]) : 
        ET.Element.set(sheet, 'reference', str(xls_sheet.row_values(9)[1]))

    # Handling required data
    EE=xls_sheet.row_values(11)[1]
    FF=xls_sheet.row_values(12)[1]
    GG=str(xls_sheet.row_values(13)[1])
    HH=str(int(xls_sheet.row_values(14)[1]))

    ET.SubElement(sheet, "AT-1").text = EE
    ET.SubElement(sheet, "AT-2").text = FF
    ET.SubElement(sheet, "keyword").text = GG
    ET.SubElement(sheet, "N").text = HH

    # Handling optional data
    if (xls_sheet.row_values(15)[1]) :
	ET.SubElement(sheet, "fplo").text = str(xls_sheet.row_values(15)[1])
    if (xls_sheet.row_values(16)[1]) :
	ET.SubElement(sheet, "fphi").text = str(xls_sheet.row_values(16)[1])
    if (xls_sheet.row_values(17)[1]) :
	ET.SubElement(sheet, "EQ").text = str(xls_sheet.row_values(17)[1])

    # Row 19 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(19))

    for row_num in xrange(20, xls_sheet.nrows):
	force_integer_idx1 = xls_sheet_header.index("index")
        cur_entry = ET.SubElement(sheet, "Bond")
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		else :
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelAnglePotential_Tabular(sheet, sub_root): 
    ''' Reads in the AnglePotential-Tabular sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    # Handling attributes
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "AnglePotential-Tabular", {'style':AA, 'angle-units':BB, 'energy-units':CC, 'energy-diff-units':DD})

    # Handling comments, version, and reference
    if (xls_sheet.row_values(7)[1]) :
        ET.Element.set(sheet, 'comment', str(xls_sheet.row_values(7)[1]))
    if (xls_sheet.row_values(8)[1]) : 
        ET.Element.set(sheet, 'version', str(xls_sheet.row_values(8)[1]))
    if (xls_sheet.row_values(9)[1]) : 
        ET.Element.set(sheet, 'reference', str(xls_sheet.row_values(9)[1]))

    # Handling required data
    EE=xls_sheet.row_values(11)[1]
    FF=xls_sheet.row_values(12)[1]
    GG=xls_sheet.row_values(13)[1]
    HH=str(xls_sheet.row_values(14)[1])
    II=str(int(xls_sheet.row_values(15)[1]))

    ET.SubElement(sheet, "AT-1").text = EE
    ET.SubElement(sheet, "AT-2").text = FF
    ET.SubElement(sheet, "AT-3").text = GG
    ET.SubElement(sheet, "keyword").text = HH
    ET.SubElement(sheet, "N").text = II

    # Handling optional data
    if (xls_sheet.row_values(16)[1]) :
	ET.SubElement(sheet, "fplo").text = str(xls_sheet.row_values(16)[1])
    if (xls_sheet.row_values(17)[1]) :
	ET.SubElement(sheet, "fphi").text = str(xls_sheet.row_values(17)[1])
    if (xls_sheet.row_values(18)[1]) :
	ET.SubElement(sheet, "EQ").text = str(xls_sheet.row_values(18)[1])

    # Row 20 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(20))

    for row_num in xrange(21, xls_sheet.nrows):
	force_integer_idx1 = xls_sheet_header.index("index")
        cur_entry = ET.SubElement(sheet, "Angle")
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		else :
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelDihedralPotential_Tabular(sheet, sub_root): 
    ''' Reads in the DihedralPotential-Tabular sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    # Handling attributes
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-Tabular", {'style':AA, 'angle-units':BB, 'energy-units':CC, 'energy-diff-units':DD})

    # Handling comments, version, and reference
    if (xls_sheet.row_values(7)[1]) :
        ET.Element.set(sheet, 'comment', str(xls_sheet.row_values(7)[1]))
    if (xls_sheet.row_values(8)[1]) : 
        ET.Element.set(sheet, 'version', str(xls_sheet.row_values(8)[1]))
    if (xls_sheet.row_values(9)[1]) : 
        ET.Element.set(sheet, 'reference', str(xls_sheet.row_values(9)[1]))

    # Handling required data
    EE=xls_sheet.row_values(11)[1]
    FF=xls_sheet.row_values(12)[1]
    GG=xls_sheet.row_values(13)[1]
    HH=xls_sheet.row_values(14)[1]
    II=str(xls_sheet.row_values(15)[1])
    JJ=str(int(xls_sheet.row_values(16)[1]))

    ET.SubElement(sheet, "AT-1").text = EE
    ET.SubElement(sheet, "AT-2").text = FF
    ET.SubElement(sheet, "AT-3").text = GG
    ET.SubElement(sheet, "AT-4").text = HH
    ET.SubElement(sheet, "keyword").text = II
    ET.SubElement(sheet, "N").text = JJ

    # Handling optional data
    if (xls_sheet.row_values(17)[1]) :
	ET.SubElement(sheet, "NOF").text = str(xls_sheet.row_values(17)[1])
    if (xls_sheet.row_values(18)[1]) :
	ET.SubElement(sheet, "CHECKU").text = str(xls_sheet.row_values(18)[1])
    if (xls_sheet.row_values(19)[1]) :
	ET.SubElement(sheet, "CHECKF").text = str(xls_sheet.row_values(19)[1])

    # Row 21 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(21))

    for row_num in xrange(22, xls_sheet.nrows):
	force_integer_idx1 = xls_sheet_header.index("index")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		else :
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

def ReadExcelNonBondPotential_Tabular(sheet, sub_root): 
    ''' Reads in the NonBondPotential-Tabular sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    # Handling attributes
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-Tabular", {'style':AA, 'Interpolation-style':BB, 'r-units':CC, 'angle-units':DD, 'force-units':EE})

    # Handling comments, version, and reference
    if (xls_sheet.row_values(8)[1]) :
        ET.Element.set(sheet, 'comment', str(xls_sheet.row_values(7)[1]))
    if (xls_sheet.row_values(9)[1]) : 
        ET.Element.set(sheet, 'version', str(xls_sheet.row_values(8)[1]))
    if (xls_sheet.row_values(10)[1]) : 
        ET.Element.set(sheet, 'reference', str(xls_sheet.row_values(9)[1]))

    # Handling required data
    FF=xls_sheet.row_values(12)[1]
    GG=xls_sheet.row_values(13)[1]
    HH=xls_sheet.row_values(14)[1]
    II=str(int(xls_sheet.row_values(15)[1]))

    ET.SubElement(sheet, "AT-1").text = FF
    ET.SubElement(sheet, "AT-2").text = GG
    ET.SubElement(sheet, "keyword").text = HH
    ET.SubElement(sheet, "N").text = II

    # Handling optional data
    if (xls_sheet.row_values(16)[1]) :
	ET.SubElement(sheet, "rlo").text = str(xls_sheet.row_values(16)[1])
    if (xls_sheet.row_values(17)[1]) :
	ET.SubElement(sheet, "rhi").text = str(xls_sheet.row_values(17)[1])
    if (xls_sheet.row_values(18)[1]) :
	ET.SubElement(sheet, "fplo").text = str(xls_sheet.row_values(18)[1])
    if (xls_sheet.row_values(19)[1]) :
	ET.SubElement(sheet, "fphi").text = str(xls_sheet.row_values(19)[1])

    # Row 21 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(21))

    for row_num in xrange(22, xls_sheet.nrows):
	force_integer_idx1 = xls_sheet_header.index("index")
        cur_entry = ET.SubElement(sheet, "NonBond")
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
		else :
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
				
def ReadExcelAutoEquivalenceTable(sheet, sub_root): 
    ''' Reads in the Equivalence-Table sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    # Row 4 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(4))

    for row_num in xrange(5, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sub_root, "AutoEquivalence")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)   
#WaterModel function
def ReadExcelWaterPotential_3Site(sheet, sub_root): 
    ''' Reads in the WaterPotential-3Site sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(2)[1]
    FF=xls_sheet.row_values(3)[1]
    GG=xls_sheet.row_values(4)[1]
    HH=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "WaterPotential-3Site", {'Style':AA, 'Formula':BB, 'R-units':CC, 'Theta_HOH-units':DD, 'A-units':EE, 'B-units':FF, 'Version':GG, 'Comment': HH})

    # Row 11 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(11))

    for row_num in xrange(12, xls_sheet.nrows):
        cur_entry = sub_root
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if "\u2212" in repr(cell_value): 
                a = repr(cell_value)
                c = a.encode("utf-8", "ignore")
                b = (c.replace("u'\u2212", '-'))
                b = (b.replace("'", ''))
                cell_value = float (b)
            if (len(str(cell_value))!=0) :
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
def ReadExcelWaterPotential_4Site(sheet, sub_root): 
    ''' Reads in the WaterPotential-4Site sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(2)[1]
    FF=xls_sheet.row_values(3)[1]
    GG=xls_sheet.row_values(4)[1]
    HH=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "WaterPotential-4Site", {'Style':AA, 'Formula':BB, 'R-units':CC, 'Theta_HOH-units':DD, 'A-units':EE, 'B-units':FF, 'Version':GG, 'Comment': HH})

    # Row 11 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(11))

    for row_num in xrange(12, xls_sheet.nrows):
        cur_entry = sub_root
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if "\u2212" in repr(cell_value): 
                a = repr(cell_value)
                c = a.encode("utf-8", "ignore")
                b = (c.replace("u'\u2212", '-'))
                b = (b.replace("'", ''))
                cell_value = float (b)
            if (len(str(cell_value))!=0) :
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
def ReadExcelWaterPotential_5Site(sheet, sub_root): 
    ''' Reads in the WaterPotential-5Site sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(2)[1]
    FF=xls_sheet.row_values(3)[1]
    GG=xls_sheet.row_values(4)[1]
    HH=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "WaterPotential-5Site", {'Style':AA, 'Formula':BB, 'R-units':CC, 'Theta_HOH-units':DD, 'A-units':EE, 'B-units':FF, 'Version':GG, 'Comment': HH})

    # Row 11 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(11))

    for row_num in xrange(12, xls_sheet.nrows):
        cur_entry = sub_root
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if "\u2212" in repr(cell_value): 
                a = repr(cell_value)
                c = a.encode("utf-8", "ignore")
                b = (c.replace("u'\u2212", '-'))
                b = (b.replace("'", ''))
                cell_value = float (b)
            if (len(str(cell_value))!=0) :
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)

# The set of functions below (all begin with XMLToParams) convert XML to .params format
def XMLToParamsNonBondPotential_LJ_Rmin(root, output_file):
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(Lennard-Jones) = Eps,i,j[(Rmin,i,j/ri,j)**12 - 2(Rmin,i,j/ri,j)**6]\n!\n" )
    f.write("!epsilon: " + ((root.find('./NonBondPotential/NonBond-LJ-Rmin')).attrib['epsilon-units']).encode('utf-8')+", ")
    f.write("Eps,i,j = sqrt(eps,i * eps,j)\n")
    f.write("!Rmin/2: "+ ((root.find('./NonBondPotential/NonBond-LJ-Rmin')).attrib['Rmin-units']).encode('utf-8')+", ")
    f.write("Rmin,i,j = Rmin/2,i + Rmin/2,j\n")
    for nonbond in root.findall('./NonBondPotential/NonBond-LJ-Rmin/NonBond'):
        if len(str(nonbond.find("AtomType")))!=0 and str(nonbond.find("AtomType")) != "None":
            f.write( nonbond.find("AtomType").text.ljust(6))
        else:
            f.write("".ljust(6))
        #Insert a column of Zeros purely for formatting purposes
        f.write(("%.6f" %0).rjust(0))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" % float(nonbond.find("epsilon").text)).rjust(12))
        else:
            f.write("".rjust(12))
        if len(str(nonbond.find("Rmin")))!=0 and str(nonbond.find("Rmin")) != "None":
            f.write(("%.6f" % float(nonbond.find("Rmin").text)).rjust(11))
        else:
            f.write("".rjust(11))
        f.write("\n") 

def XMLToParamsBondPotential_Harmonic(root, output_file):
    f = output_file
    f.write("BONDS\n!\n" )
    f.write("!V(bond) = Kb(b - b0)**2\n!\n")
    f.write("!Kb: " + ((root.find('./BondPotential/BondPotential-Harmonic')).attrib['K-units']).encode('utf-8')+"\n")
    f.write("!b0: " + ((root.find('./BondPotential/BondPotential-Harmonic')).attrib['R0-units']).encode('utf-8')+"\n!\n")
    for bond in root.findall('./BondPotential/BondPotential-Harmonic/Bond'):
        if len(str(bond.find("AT-1")))!=0 and str(bond.find("AT-1")) != "None":
            f.write(bond.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(bond.find("AT-2")))!=0 and str(bond.find("AT-2")) != "None":
            f.write(bond.find("AT-2").text.ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(bond.find("K")))!=0 and str(bond.find("K")) != "None": 
            f.write(("%.3f" %float(bond.find("K").text)).rjust(8))
        else:
            f.write("".rjust(8))
        if len(str(bond.find("R0")))!=0 and str(bond.find("R0")) != "None": 
            f.write(("%.4f" %float(bond.find("R0").text)).rjust(11))
        else:
            f.write("".rjust(11))
       
        f.write("\n")     
        
def XMLToParamsAnglePotential_Harmonic(root, output_file):
    f = output_file
    f.write("ANGLES\n!\n" )
    f.write("!V(angle) = Ktheta(Theta - Theta0)**2\n!\n")
    f.write("!Ktheta: " + ((root.find('./AnglePotential/AnglePotential-Harmonic')).attrib['Ka-units']).encode('utf-8')+"\n")
    f.write("!Theta0: " + ((root.find('./AnglePotential/AnglePotential-Harmonic')).attrib['Theta0-units']).encode('utf-8')+"\n!\n")
    for angle in root.findall('./AnglePotential/AnglePotential-Harmonic/Angle'):
        if len(str(angle.find("AT-1")))!=0 and str(angle.find("AT-1")) != "None":
         f.write(angle.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-2")))!=0 and str(angle.find("AT-2")) != "None":
            f.write(angle.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-3")))!=0 and str(angle.find("AT-3")) != "None":
            f.write(angle.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("Ka")))!=0 and str(angle.find("Ka")) != "None": 
            f.write(("%.3f" %float(angle.find("Ka").text)).rjust(7))
        else:
            f.write("".rjust(7))
        if len(str(angle.find("Theta0")))!=0 and str(angle.find("Theta0")) != "None": 
            f.write(("%.2f" %float(angle.find("Theta0").text)).rjust(11))
        else: 
            f.write("".rjust(11))
        
        f.write("\n")
def XMLToParamsDihedralPotential_CHARMM(root, output_file):
    f = output_file
    f.write("DIHEDRALS\n!\n" )
    f.write("!V(dihedral) = Kchi(1 + cos(n(chi) + delta))\n!\n")
    f.write("!Kchi: " + ((root.find('./DihedralPotential/DihedralPotential-CHARMM')).attrib['Kd-units']).encode('utf-8')+"\n")
    f.write("!n: multiplicity\n")
    f.write("!delta: " + ((root.find('./DihedralPotential/DihedralPotential-CHARMM')).attrib['Phi0-units']).encode('utf-8')+"\n!\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-CHARMM/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(dihedral.find("Kd")))!=0 and str(dihedral.find("Kd")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("Kd").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("N")))!=0 and str(dihedral.find("N")) != "None": 
            f.write(("%.0f"%float((dihedral.find("N").text))).ljust(4))
        else:
            f.write("".ljust(4))
        if len(str(dihedral.find("Phi0")))!=0 and str(dihedral.find("Phi0")) != "None": 
            f.write(("%.3f" %float(dihedral.find("Phi0").text)).rjust(7))
        else:
            f.write("".rjust(7))
        f.write("\n")
def XMLToParamsImproperPotential_Harmonic(root, output_file):
    f = output_file
    f.write("IMPROPER\n!\n")
    f.write("!V(improper) = Kpsi(psi - psi0)**2\n!\n" )
    f.write("!Kpsi: " + ((root.find('./ImproperPotential/ImproperPotential-Harmonic')).attrib['Ki-units']).encode('utf-8')+"\n")
    f.write("!psi0: "+ ((root.find('./ImproperPotential/ImproperPotential-Harmonic')).attrib['Chi0-units']).encode('utf-8')+"\n")
    f.write("!note that the second column of numbers (0) is ignored\n!\n")
        
    for improper in root.findall('./ImproperPotential/ImproperPotential-Harmonic/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
            f.write(improper.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.5f" %float(improper.find("Ki").text)).rjust(8))
        else:
            f.write("".rjust(8))
        f.write((str(0)).rjust(4))
        if len(str(improper.find("Chi0")))!=0 and str(improper.find("Chi0")) != "None": 
            f.write(("%.4f" %float(improper.find("Chi0").text)).rjust(11))
        else:
            f.write("".rjust(11))
        f.write("\n")
def XMLToParamsAtomTypes(root, output_file):
    f = output_file
    f.write("MASSES\n")
    masses = []
    for atomType in root.findall('./AtomTypes/AtomType'):
        if "AtomicMass" in atomType.attrib.keys() and atomType.find("AtomType-Name").text not in masses: 
            f.write((atomType.find("AtomType-Name").text) + " " + "%.5f" %float(atomType.attrib["AtomicMass"]))
            masses.append(atomType.find("AtomType-Name").text)
            f.write("\n") 
# The set of functions below (all begin with XMLToFrc) convert XML to .frc format
def XMLtoFrcAtomTypes(root, output_file): 
    f = output_file
    f.write("#atom_types \n\n" )
    f.write("> Atom type definitions (set the mass of atom types)\n\n")
    f.write("!Ver  Ref  Type    Mass      Element  Connection   Comment\n")
    f.write("!---- ---  ----  ----------  -------  -----------  ----------------------------\n")
    for atomtype in root.findall('./AtomTypes/AtomType'):
        if "version" in atomtype.attrib.keys():
            f.write(" " +atomtype.attrib["version"].ljust(7))
        else:
            f.write(" ".ljust(7))
        if "reference" in atomtype.attrib.keys():
            f.write(atomtype.attrib["reference"].ljust(4))
        else:
            f.write("".ljust(4))
        if len(str(atomtype.find("AtomType-Name")))!=0 and str(atomtype.find("AtomType-Name")) != "None":
            f.write(atomtype.find("AtomType-Name").text.ljust(7))
        else:
            f.write("".ljust(7))
        if "AtomicMass"in atomtype.attrib.keys():
            f.write(("%.3f" %float(atomtype.attrib["AtomicMass"])).rjust(6))
        else:
            f.write("".rjust(6))
        if "Element" in atomtype.attrib.keys(): 
            f.write(atomtype.attrib["Element"].rjust(8))
        else:
            f.write("".rjust(8))
        if "Connection" in atomtype.attrib.keys(): 
            f.write(atomtype.attrib["Connection"].rjust(10))
        else:
            f.write("".rjust(10))
        f.write("".rjust(10))
        if "Description" in atomtype.attrib.keys(): 
            f.write(atomtype.attrib["Description"].ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n") 
def XMLtoFrcEquivalenceTable(root, output_file): 
    f = output_file
    f.write("#\n#equivalence\n\n" )
    f.write("> Equivalence table\n\n")
    f.write("!                                 Equivalences\n")
    f.write("!                 -----------------------------------------\n")
    f.write("!Ver  Ref   Type  NonB     Bond    Angle    Torsion    OOP\n")
    f.write("!---- ---   ----  ----     ----    -----    -------    ----\n")
    for equivalence in root.findall('./EquivalenceTable/Equivalence-Table'):
        if "version" in equivalence.attrib.keys():
            f.write(" " +equivalence.attrib["version"].ljust(6))
        else:
            f.write(" ".ljust(6))
        if "reference" in equivalence.attrib.keys():
            f.write(("%.0f" %float(equivalence.attrib["reference"])).ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(equivalence.find("AtomType")))!=0 and str(equivalence.find("AtomType")) != "None":
            f.write(equivalence.find("AtomType").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(equivalence.find("NonBond")))!=0 and str(equivalence.find("NonBond")) != "None":
            f.write(equivalence.find("NonBond").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(equivalence.find("Bond")))!=0 and str(equivalence.find("Bond")) != "None": 
            f.write(equivalence.find("Bond").text.ljust(9))
        else:
            f.write("".ljust(8))
        if len(str(equivalence.find("Angle")))!=0 and str(equivalence.find("Angle")) != "None": 
            f.write(equivalence.find("Angle").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(equivalence.find("Dihedral")))!=0 and str(equivalence.find("Dihedral")) != "None": 
            f.write(equivalence.find("Dihedral").text.ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(equivalence.find("Improper")))!=0 and str(equivalence.find("Improper")) != "None": 
            f.write(equivalence.find("Improper").text.ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n") 
def XMLtoFrcBondPotential_Harmonic(root, output_file): 
    f = output_file
    f.write("#quadratic_bond\n\n" )
    f.write("> E = kb*(b-b0)^2\n\n")
    f.write("!Ver  Ref     I     J      b0      kb\n")
    f.write("!---- ---    ----  ----  -----   -------\n")
    for bond in root.findall('./BondPotential/BondPotential-Harmonic/Bond'):
        if "version" in bond.attrib.keys():
            f.write(" " +bond.attrib["version"].ljust(6))
        else:
            f.write(" ".ljust(6))
        if "reference" in bond.attrib.keys():
            f.write(("%.0f" %float(bond.attrib["reference"])).ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(bond.find("AT-1")))!=0 and str(bond.find("AT-1")) != "None":
            f.write(bond.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(bond.find("AT-2")))!=0 and str(bond.find("AT-2")) != "None":
            f.write(bond.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(bond.find("R0")))!=0 and str(bond.find("R0")) != "None": 
            f.write(("%.4f" %float(bond.find("R0").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(bond.find("K")))!=0 and str(bond.find("K")) != "None": 
            f.write(("%.1f" %float(bond.find("K").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n") 
def XMLtoFrcAnglePotential_Harmonic(root, output_file): 
    f = output_file
    f.write("#quadratic_angle\n\n" )
    f.write("> E = K2 * (th - th0)^2\n\n")
    f.write("!Ver  Ref     I     J    K      th0        K2\n")
    f.write("!---- ---    ----  ---- ----   ------    ---------\n")
    for angle in root.findall('./AnglePotential/AnglePotential-Harmonic/Angle'):
        if "version" in angle.attrib.keys():
            f.write(" " +angle.attrib["version"].ljust(6))
        else:
            f.write(" ".ljust(6))
        if "reference" in angle.attrib.keys():
            f.write(("%.0f" %float(angle.attrib["reference"])).ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-1")))!=0 and str(angle.find("AT-1")) != "None":
            f.write(angle.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-2")))!=0 and str(angle.find("AT-2")) != "None":
            f.write(angle.find("AT-2").text.ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(angle.find("AT-3")))!=0 and str(angle.find("AT-3")) != "None":
            f.write(angle.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(angle.find("Theta0")))!=0 and str(angle.find("Theta0")) != "None": 
            f.write(("%.2f" %float(angle.find("Theta0").text)).ljust(10))
        else: 
            f.write("".ljust(10))
        if len(str(angle.find("Ka")))!=0 and str(angle.find("Ka")) != "None": 
            f.write(("%.2f" %float(angle.find("Ka").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n") 
def XMLtoFrcImproperPotential_CHARMM(root, output_file): 
    f = output_file
    f.write("#out_of_plane\n\n" )
    f.write("> E = K1*[1+cos(n*Phi+Phi0)]\n\n")
    f.write("!Ver  Ref    I      J      K      L        K1        n       Phi0\n")
    f.write("!---- ---  -----  -----  -----  -----   -------   --------- -------\n")
    for improper in root.findall('./ImproperPotential/ImproperPotential-CHARMM/Improper'):
        if "version" in improper.attrib.keys():
            f.write(" " +improper.attrib["version"].ljust(6))
        else:
            f.write(" ".ljust(6))
        if "reference" in improper.attrib.keys():
            f.write(("%.0f" %float(improper.attrib["reference"])).ljust(4))
        else:
            f.write("".ljust(4))
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Kd")))!=0 and str(improper.find("Kd")) != "None": 
            f.write(("%.6f" %float(improper.find("Kd").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("N")))!=0 and str(improper.find("N")) != "None": 
            f.write(("%.1f" %float(improper.find("N").text)).ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(improper.find("Phi0")))!=0 and str(improper.find("Phi0")) != "None": 
            f.write(("%.1f" %float(improper.find("Phi0").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
def XMLtoFrcDihedralPotential_FourierSimple(root, output_file):    
    f = output_file
    f.write("##torsion_4\n\n" )
    f.write("> E = K1*[1+cos(Phi)] + K2*[1+cos(2*Phi)] + K3*[1+cos(3*Phi)] + K4*[1+cos(4*Phi)]\n\n")
    f.write("!Ver  Ref    I      J      K      L        K1         K2         K3         K4        K5\n")
    f.write("!---- ---  -----  -----  -----  -----   --------   --------   --------   --------   --------\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-FourierSimple/Dihedral'):
        if "version" in dihedral.attrib.keys():
            f.write(" " +dihedral.attrib["version"].ljust(6))
        else:
            f.write(" ".ljust(6))
        if "reference" in dihedral.attrib.keys():
            f.write(("%.0f" %float(dihedral.attrib["reference"])).ljust(4))
        else:
            f.write("".ljust(4))
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("K1")))!=0 and str(dihedral.find("K1")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K1").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("K2")))!=0 and str(dihedral.find("K2")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K2").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("K3")))!=0 and str(dihedral.find("K3")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K3").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("K4")))!=0 and str(dihedral.find("K4")) != "None" : 
            f.write(("%.6f" %float(dihedral.find("K4").text)).rjust(11))
        else:
            f.write("".rjust(11)) 
        if len(str(dihedral.find("K5")))!=0 and str(dihedral.find("K5")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K5").text)).rjust(11))
        else:
            f.write("".rjust(11))
        f.write("\n")
    f.write("\n")
def XMLtoFrcNonBond_LJ(root, output_file):
    f = output_file
    f.write("#nonbond(12-6)\n\n" )
    f.write("@type r-eps\n@combination geometric\n\n" )
    f.write("> E = 4*eps((sigma/r)^12 - (sigma/r)^6)\n\n")
    f.write("!Ver  Ref     I        sigma       eps       \n")
    f.write("!---- ---    ----    ---------  ---------   \n")
    for nonbond in root.findall('./NonBondPotential/NonBond-LJ/NonBond'):
        if "version" in nonbond.attrib.keys():
            f.write(" " +nonbond.attrib["version"].ljust(6))
        else:
            f.write(" ".ljust(6))
        if "reference" in nonbond.attrib.keys():
            f.write(("%.0f" %float(nonbond.attrib["reference"])).ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(nonbond.find("AtomType")))!=0 and str(nonbond.find("AtomType")) != "None":
            f.write(nonbond.find("AtomType").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
def XMLtoFrcBondIncrements(root, output_file):
    f = output_file
    f.write("##bond_increments\n\n" )
    f.write("!Ver  Ref     I     J       DeltaIJ     DeltaJI\n")
    f.write("!---- ---    ----  ----     -------     -------\n")
    for increment in root.findall('./BondIncrements/Bond-Increments'):
        if "version" in increment.attrib.keys():
                f.write(" " +increment.attrib["version"].ljust(6))
        else:
             f.write(" ".ljust(6))
        if "reference" in increment.attrib.keys():
             f.write(("%.0f" %float(increment.attrib["reference"])).ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(increment.find("AT-I")))!=0 and str(increment.find("AT-I")) != "None":
            f.write(increment.find("AT-I").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(increment.find("AT-J")))!=0 and str(increment.find("AT-J")) != "None":
            f.write(increment.find("AT-J").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(increment.find("Delta-IJ")))!=0 and str(increment.find("Delta-IJ")) != "None":
            f.write(increment.find("Delta-IJ").text.ljust(12))
        else:
            f.write("".ljust(12))
        if len(str(increment.find("Delta-JI")))!=0 and str(increment.find("Delta-JI")) != "None": 
            f.write(increment.find("Delta-JI").text.ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    
# The functions below create a file with citation information taken from an XML file and outputed as a text file 
def XMLtoCitBib(root, output_file): 
    f = output_file
    if(root.find("./Force-Field-Header/Data-Source/Compact/Reference") != None):
        citation = (root.find("./Force-Field-Header/Data-Source/Compact/Reference").text)
    if(root.find("./Force-Field-Header/Data-Source/Compact/DOI") != None):
        DOI = (root.find("./Force-Field-Header/Data-Source/Compact/DOI").text)
    f.write("You have downloaded data from webff.nist.gov, if you use this data in any publication please cite the following sources: \n")
    f.write("Data source citation: webff.nist.gov\n")
    f.write("Data source publication: TBA\n")
    f.write("Force-field data citation: "+ citation +", "+ DOI+ "\n" )