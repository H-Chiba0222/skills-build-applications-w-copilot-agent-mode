document.addEventListener('DOMContentLoaded',()=>{
  const form=document.getElementById('activity-form')
  const input=document.getElementById('activity-input')
  const list=document.getElementById('activity-list')

  function addItem(text){
    const li=document.createElement('li')
    li.textContent=text
    list.prepend(li)
  }

  form.addEventListener('submit',e=>{
    e.preventDefault()
    const val=input.value.trim()
    if(!val) return
    addItem(val)
    input.value=''
  })

  // sample starter items
  ['ランニング 5km','サイクリング 20km'].forEach(addItem)
})
