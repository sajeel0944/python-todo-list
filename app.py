import streamlit as st

st.set_page_config(page_title="Todo List")

# Title for the app
st.title("Welcome to ToDoList")

# is ky andar sary task aye gy
if 'todos' not in st.session_state:
    st.session_state.todos = []

# is ko liye dia hai jab user nichy input filed par number dy ga to is ky zayeye check hoye ga
manage_opt = [
    "Add task", "View task", "Remove task", "Exit"
]

# ye ui par show ho rahe hai 
st.write("1 : Add task")
st.write("2 : View task")
st.write("3 : Remove task")
st.write("4 : Exit")

# user selecte kary ga u sy kon sa option selecte karna hai
sele_option = st.text_input("💫 Enter your option (1-4):")

# user ny number ky alawa string ya kuch or di a to else chaly ga
if sele_option and sele_option.isdigit():
    sele_option = int(sele_option)
    
    # ye check kary ga ky user ny jo number dia hai wo 1 to 4 ky bich main sy dia hai agar nhi to else chaly ga
    if 1 <= sele_option <= 4:
        selected_option = manage_opt[sele_option - 1]
        st.write(f"You selected: {selected_option}")

        if selected_option == "Add task":
            # Function to add a task
            def add_todo():
                todo = st.session_state.new_todo
                if todo != "": # agar user input field ky andar task dy ga to is ky zaye ye add hoye ga
                    st.session_state.todos.append(todo)
                    st.session_state.new_todo = ""  # Clear input field
                    st.warning("✅ successfully add your task")
                elif todo == "": # agar user ny input  field ky andar kucj bhi nhi dia to ye cahly ga
                    st.warning("⚠️ please add your task")
            
            # is main user apna task dyga
            task : str = st.text_input("📝 Add a new to-do item", key="new_todo")

            # Button to add task
            st.button("Add To-Do", on_click=add_todo)

           

        elif selected_option == "View task":
            # Show the tasks in the to-do list
            st.write("### 🚀 Your To-Do List:")
            # idx ky nadar task ky number arahy hai or todo ky nadar task arahy hai
            for idx, todo in enumerate(st.session_state.todos, 1):
                st.write(f"{idx}. {todo}")

        elif selected_option == "Remove task":
            # Remove a task 
            if st.session_state.todos: # agar task hoga to he ye chaly ga 
                # 
                remove_idx = st.number_input("Enter task number to remove",  min_value=1,)
                if st.button("remove"):
                    try:
                        # agar user jo number dyga us number par data hoye ga to he ye chaly ga
                        if remove_idx:
                            # Remove the task by index
                            task_removed = st.session_state.todos.pop(remove_idx - 1)
                            st.write(f"Task removed: {task_removed}") # jo task remove hoye ga wo is main aye ga
                    # agar user ny q number garak dia to ye chaly ga
                    except Exception as e:
                        st.warning("🚫 No tasks available to remove.")
            else: # agar task nhi hoye ga to ye chaly ga
                st.write("🚫 No tasks available to remove.")

        elif selected_option == "Exit":
            st.write("👋 Goodbye!")
            st.stop()  # Stop the app (exit)

    else:
        st.warning("❌ Invalid option. Please select a number between 1 and 4.")
else:
    if sele_option != "":
        st.error("❌ Input must be a number between 1 and 4.")



