const tasks=[];
const input=document.querySelector('#newtask');
const add=document.querySelector('#addtask');
const listTasks=document.querySelector('.listTasks');
add.addEventListener('click', (e)=>{
    e.preventDefault();
    if(input.value.trim()){
        tasks.push(input.value);
        let task=document.createElement('p');
        task.className='task';

        let x=document.createElement('button');
        x.className='taskdelete';
        x.textContent='X';

        task.textContent=input.value;
        task.appendChild(x);
        listTasks.appendChild(task);
        
        input.value = ''
        
        let taskText=input.value;
        x.addEventListener('click', ()=>{
            listTasks.removeChild(task);
            tasks.splice(tasks.indexOf(taskText), 1);
        })
        
    }
    
});


