Attribute VB_Name = "Module1"
Sub alphabetical_testing()

        'Define Ticker symbol
        Dim ticker_name As String
        
        'Define total for tickers
        Dim ticker_total As Double
        ticker_total = 0
        
        'Define open total for tickers
        Dim ticker_open As Double
        ticker_open = Cells(2, 3).Value

        'Define close total for tickers
        Dim ticker_close As Double
        ticker_close = 0
        
        'Define field for Yearly Change
        Dim yearly_change As Double
        yearly_change = 0
        
        'Define field for Percent Change
        Dim percent_change As Double
        percent_change = 0
        
        'Define field for total stock volume
        Dim total_stock_volume As Double
        total_stock_volume = 0
        
        'Define summary table
        Dim Summary_Table_Row As Integer
        Summary_Table_Row = 2
        ' loop apply to each worksheet

        
            'Find last row
            LastRow = Cells(Rows.Count, 1).End(xlUp).Row
        
         For i = 2 To LastRow
        
               If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
                         
                    'Set stock name
                    ticker = Cells(i, 1).Value
                    
                    'Add stock volume total
                     total_stock_volume = total_stock_volume + Cells(i, 7).Value
                    
                    'Add stock name to summary table
                    Range("I" & Summary_Table_Row).Value = ticker
                    
                    'Add stock volume
                    Range("L" & Summary_Table_Row).Value = total_stock_volume
                    
                   'Add stock volume
                   Range("L" & Summary_Table_Row).Value = total_stock_volume
               
                   'Set close price
                   ticker_close = Cells(i, 6).Value
                   
                   'Calculate yearly price
                   yearly_change = (ticker_close - ticker_open)
        
                   'Add yearly change to summary table
                   Range("J" & Summary_Table_Row).Value = yearly_change
                
                  'Calculate percentage
                   If (ticker_open = 0) Then

                        percent_change = 0

                Else
                    
                    percent_change = yearly_change / ticker_open
                
                End If

            'Add yearly percent change
              Range("K" & Summary_Table_Row).Value = percent_change
              Range("K" & Summary_Table_Row).NumberFormat = "0.00%"
   
              'Reset the row counter. Add one to the summary_ticker_row
             Summary_Table_Row = Summary_Table_Row + 1

              'Reset volume of trade to zero
              total_stock_volume = 0

              'Reset the opening price
              ticker_open = Cells(i + 1, 3)
            
            Else
              
               'Add the volume of trade
              total_stock_volume = total_stock_volume + Cells(i, 7).Value

            End If
        
        Next i

    'First find the last row of the summary table
    lastrow_summary_table = Cells(Rows.Count, 9).End(xlUp).Row
    
    'Highlight positive change in green and negative change in red.
    For i = 2 To lastrow_summary_table
            If Cells(i, 10).Value > 0 Then
                Cells(i, 10).Interior.ColorIndex = 4
            Else
                Cells(i, 10).Interior.ColorIndex = 3
            End If
        Next i

End Sub


            

