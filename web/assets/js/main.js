
(function(){
  var h=document.querySelector('.hamburguesa'),n=document.querySelector('.nav');
  if(h&&n){h.addEventListener('click',function(){var a=n.classList.toggle('abierta');h.setAttribute('aria-expanded',a)})}
  document.querySelectorAll('.desplegable>button').forEach(function(b){
    b.addEventListener('click',function(ev){ev.stopPropagation();var p=b.parentNode,a=p.classList.toggle('abierto');b.setAttribute('aria-expanded',a)})
  });
  document.addEventListener('click',function(ev){document.querySelectorAll('.desplegable.abierto').forEach(function(d){if(!d.contains(ev.target)){d.classList.remove('abierto');d.querySelector('button').setAttribute('aria-expanded','false')}})});
  document.addEventListener('keydown',function(ev){if(ev.key==='Escape'){document.querySelectorAll('.desplegable.abierto').forEach(function(d){d.classList.remove('abierto')})}});
  var q=new URLSearchParams(location.search),sv=document.getElementById('servicio'),fn=document.getElementById('funcion');if(sv&&q.get('servicio')){sv.value=q.get('servicio')}if(fn&&q.get('funcion')){fn.value=q.get('funcion')}
  var f=document.querySelector('form[data-contacto]');
  if(f){var t0=Date.now(),hum=false,tk=document.getElementById('_t'),av=document.getElementById('form-aviso');
    ['mousemove','touchstart','keydown','scroll'].forEach(function(e){window.addEventListener(e,function(){hum=true},{once:true,passive:true})});
    function aviso(m){if(av){av.textContent=m;av.hidden=false}}
    f.addEventListener('submit',function(ev){
      var bad=null,msg=(f.mensaje&&f.mensaje.value)||'',urls=(msg.match(/https?:\/\/|www\./gi)||[]).length,last=0;
      try{last=+localStorage.getItem('se_envio')||0}catch(x){}
      if(f._honey.value||f.website.value)bad='spam';
      else if(Date.now()-t0<4000)bad='Espera unos segundos antes de enviar.';
      else if(!hum)bad='Mueve el ratón o toca la pantalla y vuelve a intentarlo.';
      else if(urls>1)bad='Por seguridad, no incluyas más de un enlace en el mensaje.';
      else if(/[Ѐ-ӿ一-鿿]/.test(msg))bad='Escribe el mensaje en español o inglés.';
      else if(Date.now()-last<60000)bad='Ya has enviado un mensaje hace un momento. Espera un minuto.';
      if(bad){ev.preventDefault();if(bad!=='spam')aviso(bad);return}
      if(tk)tk.value=String(Date.now()-t0);
      try{localStorage.setItem('se_envio',String(Date.now()))}catch(x){}
      var b=f.querySelector('button[type=submit]');if(b){b.disabled=true;b.textContent='Enviando…'}
    },true);
  }
  if(f){f.addEventListener('submit',function(ev){var ok=true;f.querySelectorAll('[required]').forEach(function(i){var m=i.parentNode.querySelector('.error');if(!i.value.trim()){ok=false;if(m)m.hidden=false}else if(m){m.hidden=true}});if(!ok){ev.preventDefault()}})}
})();
