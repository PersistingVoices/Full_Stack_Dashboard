Function find_and_replace_2(sheet_name As String, _
                            to_find As String, _
                            Optional rng As String, _
                            Optional var_value As Variant, _
                            Optional var_num As Variant) As Boolean

    'sheet_name activates first if condition
    'sheet_name reps the sheet to check in
    'to_find reps the string to search and replace
    
    'optional rng activates second if condition
    'var_value reps the passed variables numerical/string value
    'var_num reps the position in arr2 where its name has been stored
    
    If Not IsMissing(rng) Then 'Case when a range has been supplied to determine _
                                value of cell
        If Worksheets(sheet_name).range(rng).Value <> "" Then
            .Application.Selection.Find.text = Chr(34) & var_string & Chr(34)
            .Application.Selection.Find.Execute
               If .Application.Selection.Find.Found = True Then
                  .Application.Selection = Worksheets(sheet_name).range(rng).Value
               End If
            .Application.Selection.EndOf
            .Application.Selection.HomeKey Unit:=6
         End If
    
    Else
    
        If Not IsMissing(var_value) Then 'Case when a value has been supplied to determine _
                                            value of cell
            If var_value <> "" Then
               .Application.Selection.Find.text = Chr(34) & var_string & Chr(34)
               .Application.Selection.Find.Execute
                 If .Application.Selection.Find.Found = True Then
                    .Application.Selection = var_value
                 End If
               .Application.Selection.EndOf
               .Application.Selection.HomeKey Unit:=6
            End If
        
        Else 'If the var_value is also missing, something is wrong. Variables have not been passed _
                into the function, end with debug print
            GoTo label:
        End If
        
    End If

label:
    Debug.Print ("No variable or range has been passed to function")
End Function