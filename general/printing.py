import numpy as np


class Printing:
    def __init__(self) -> None:
        pass
        
    def print_1d_array(self, array: np.ndarray) -> None:
        print(f'{array}\n')
                
    def print_2d_array(self, array: np.ndarray) -> None:
        print('[')
        
        for row, row_val in enumerate(array):
            print(f'  {row_val}', end='')
            
            if(row < len(array) - 1):
                print(',')

        print('\n]\n')
        
    def print_3d_array(self, array: np.ndarray) -> None:
        print('[')
        
        for width, width_val in enumerate(array):
            print('  [')
            
            for row, row_val in enumerate(width_val):
                print(f'    {row_val}', end='')
                
                if(row < len(width_val) - 1):
                    print(',')

            print('\n  ]', end = '')
            
            if(width < len(array) - 1):        
                print(',')
                
        print('\n]\n')
