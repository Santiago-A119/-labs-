import itertools


class KnapsackSolver:
    """
    Knapsack problem solver for Tom (Variant 9)
    Variant 9: 2x4 inventory (8 cells), paranoia, starting points: 20
    """

    def __init__(self):
        # Define all items: (name, size, survival points)
        self.items = {
            'r': ('rifle', 3, 25),
            'p': ('pistol', 2, 15),
            'a': ('ammo', 2, 15),
            'm': ('medkit', 2, 20),
            'i': ('inhaler', 1, 5),
            'k': ('knife', 1, 15),
            'x': ('axe', 3, 20),
            't': ('talisman', 1, 25),
            'f': ('flask', 1, 15),
            'd': ('antidot', 1, 10),
            's': ('supplies', 2, 20),
            'c': ('crossbow', 2, 20)
        }

        # Variant 9 parameters
        self.backpack_size = 8  
        self.required_item = 'd'  
        self.starting_points = 20

        self.all_items = list(self.items.keys())

    def calculate_score(self, selected_items):
        """
        Calculate final survival score for selected items
        Formula: starting_points + (points of taken items) - (points of left items)
        """
        total_score = self.starting_points

        # Add points for taken items
        for item in selected_items:
            total_score += self.items[item][2]

        # Subtract points for items left behind
        for item in self.all_items:
            if item not in selected_items:
                total_score -= self.items[item][2]

        return total_score

    def calculate_used_space(self, selected_items):
        """
        Calculate total space used by selected items
        """
        total_space = 0
        for item in selected_items:
            total_space += self.items[item][1]  
        return total_space

    def is_valid_solution(self, selected_items):
        """
        Check if item combination is a valid solution
        Must satisfy: required item present, fits in backpack, positive score
        """
        
        if self.required_item not in selected_items:
            return False

        
        if self.calculate_used_space(selected_items) > self.backpack_size:
            return False

        
        if self.calculate_score(selected_items) <= 0:
            return False

        return True

    def find_all_solutions(self):
        """
        Find all possible item combinations that satisfy all conditions
        Uses brute force by checking all possible combinations
        """
        solutions = []

        
        for r in range(1, len(self.all_items) + 1):
            
            for combination in itertools.combinations(self.all_items, r):
                selected_items = list(combination)

            
                if self.is_valid_solution(selected_items):
                    solutions.append(selected_items)

        return solutions

    def display_inventory(self, selected_items):
        """
        Display inventory as 2x4 grid with item codes in brackets
        """
        # Create empty 2x4 grid
        grid = [['[ ]', '[ ]', '[ ]', '[ ]'],
                ['[ ]', '[ ]', '[ ]', '[ ]']]

        
        current_pos = 0
        for item in selected_items:
            size = self.items[item][1]

            # Place item in consecutive cells
            for i in range(size):
                row = current_pos // 4 
                col = current_pos % 4  
                grid[row][col] = f'[{item}]'
                current_pos += 1

        # Print the grid
        print("Инвентарь Тома (2x4):")
        for row in grid:
            print(' '.join(row))

    def solve_7_cell_problem(self):
        """
        ДОПЗАДАНИЕ: Find solutions for 7-cell inventory
        """
        print("\n" + "="*50)
        print("ДОПЗАДАНИЕ: РЕШЕНИЕ ДЛЯ 7 ЯЧЕЕК")
        print("="*50)

        solutions_7 = []
        original_size = self.backpack_size

        # Temporarily change backpack size to 7 cells
        self.backpack_size = 7

        
        for r in range(1, len(self.all_items) + 1):
            for combination in itertools.combinations(self.all_items, r):
                selected_items = list(combination)
                if self.is_valid_solution(selected_items):
                    solutions_7.append(selected_items)

        
        self.backpack_size = original_size

        return solutions_7

    def display_item_info(self):
        """
        Display information about all available items
        """
        print("\nAvailable items:")
        for code, (name, size, points) in self.items.items():
            print(f"  {code}: {name:10} | Size: {size} | Points: {points}")

    def run(self):
        """
        Main method to run the solver and display results
        """
        print("=== ЛАБОРАТОРНАЯ РАБОТА №4 - ВАРИАНТ 9 ===")
        print("Parameters:")
        print(f"- Inventory size: 2x4 ({self.backpack_size} cells)")
        print(
            f"- Required item: {self.items[self.required_item][0]} ({self.required_item})")
        print(f"- Starting points: {self.starting_points}")
        print("="*50)

    
        self.display_item_info()
        solutions = self.find_all_solutions()

        if not solutions:
            print("\nNo solutions found!")
            return

        print(f"\nFound solutions: {len(solutions)}")

        
        best_solution = max(solutions, key=lambda x: self.calculate_score(x))
        best_score = self.calculate_score(best_solution)

        print(f"\nЛУЧШЕЕ РЕШЕНИЕ (points: {best_score}):")
        self.display_inventory(best_solution)

        
        print("\nItem breakdown:")
        total_space = 0
        total_points = self.starting_points
        for item in best_solution:
            name, size, points = self.items[item]
            total_space += size
            total_points += points
            print(f"  {name} ({item}): {size} cell(s), +{points} points")

        
        lost_points = 0
        for item in self.all_items:
            if item not in best_solution:
                lost_points += self.items[item][2]

        print(f"\nUsed space: {total_space}/{self.backpack_size}")
        print(f"Starting points: {self.starting_points}")
        print(f"Points gained: {total_points - self.starting_points}")
        print(f"Points lost from left items: -{lost_points}")
        print(f"Final score: {best_score}")

        
        print(f"\nВСЕ РЕШЕНИЯ ({len(solutions)} combinations):")
        for i, solution in enumerate(solutions, 1):
            score = self.calculate_score(solution)
            space = self.calculate_used_space(solution)
            items_str = ', '.join(solution)
            print(f"{i:2d}. Score: {score:3d}, Space: {space}/8, Items: {items_str}")

        
        solutions_7 = self.solve_7_cell_problem()

        if solutions_7:
            print(f"\nSolutions found for 7 cells: {len(solutions_7)}")
        
            best_7 = max(solutions_7, key=lambda x: self.calculate_score(x))
            best_7_score = self.calculate_score(best_7)
            best_7_space = self.calculate_used_space(best_7)
            print(f"Best solution for 7 cells:")
            print(f"  Score: {best_7_score}, Space: {best_7_space}/7")
            print(f"  Items: {', '.join(best_7)}")

        
            print(f"\nAll solutions for 7 cells:")
            for i, solution in enumerate(solutions_7, 1):
                score = self.calculate_score(solution)
                space = self.calculate_used_space(solution)
                items_str = ', '.join(solution)
                print(
                    f"  {i:2d}. Score: {score:3d}, Space: {space}/7, Items: {items_str}")
        else:
            print("\nNo solutions found for 7 cells!")


if __name__ == "__main__":
    solver = KnapsackSolver()
    solver.run()
