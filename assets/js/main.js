function selectAccountType(type) {
    document.querySelectorAll('.account-type-option').forEach(el => el.classList.remove('selected'));
    document.getElementById('type-' + type).classList.add('selected');
    document.getElementById('btn-proceed').disabled = false;
    window.selectedAccountType = type;
  }
  
  function proceedToLoginMethod() {
    document.getElementById('login-step-0').classList.add('hidden');
    document.getElementById('login-step-1').classList.remove('hidden');
    
    if(window.selectedAccountType === 'corporate') {
      document.getElementById('account-type-display').innerHTML = 'Corporate Employee Account';
      document.getElementById('corporate-login-options').classList.remove('hidden');
    } else {
      document.getElementById('account-type-display').innerHTML = 'Individual Account';
      document.getElementById('corporate-login-options').classList.add('hidden');
    }
    selectLoginMethod('phone');
  }

  function backToStep(step) {
    document.getElementById('login-step-1').classList.add('hidden');
    document.getElementById('login-step-2').classList.add('hidden');
    document.getElementById('login-step-' + step).classList.remove('hidden');
  }

  function selectLoginMethod(method) {
    document.querySelectorAll('.login-method-btn').forEach(el => el.classList.remove('active'));
    document.getElementById('method-' + method).classList.add('active');
    
    document.querySelectorAll('.login-form').forEach(el => el.classList.add('hidden'));
    document.getElementById('login-' + method).classList.remove('hidden');
  }

  function sendOTP(method) {
    document.getElementById('login-step-1').classList.add('hidden');
    document.getElementById('login-step-2').classList.remove('hidden');
    if(method === 'phone') document.getElementById('otp-destination').innerHTML = document.getElementById('phone-input').value || '+91 9876543210';
    if(method === 'aadhaar') document.getElementById('otp-destination').innerHTML = 'Aadhaar linked number';
    if(method === 'employee-id') document.getElementById('otp-destination').innerHTML = document.getElementById('corp-email-input').value || 'Corporate Email';
  }

  function moveToNext(current) {
    if(document.getElementById('otp-'+current).value.length === 1 && current < 6) {
      document.getElementById('otp-'+(current+1)).focus();
    }
  }

  function verifyOTP() {
    document.getElementById('login-fullscreen').style.display = 'none';
    document.getElementById('main-sidebar').style.display = 'block';
    document.getElementById('main-content').style.display = 'block';
    
    if(window.selectedAccountType === 'corporate') {
      document.getElementById('user-name').innerHTML = 'Welcome, Rahul Sharma (EMP001234)';
      document.getElementById('user-type').innerHTML = 'Corporate Member - TCS';
      document.getElementById('nav-corporate-benefits').style.display = 'block';
      document.getElementById('individual-dashboard').classList.add('hidden');
      document.getElementById('corporate-dashboard').classList.remove('hidden');
      document.getElementById('individual-policies').classList.add('hidden');
      document.getElementById('corporate-policies').classList.remove('hidden');
    } else {
      document.getElementById('user-name').innerHTML = 'Welcome, Rahul Sharma';
      document.getElementById('user-type').innerHTML = 'Individual Member';
      document.getElementById('nav-corporate-benefits').style.display = 'none';
      document.getElementById('individual-dashboard').classList.remove('hidden');
      document.getElementById('corporate-dashboard').classList.add('hidden');
      document.getElementById('individual-policies').classList.remove('hidden');
      document.getElementById('corporate-policies').classList.add('hidden');
    }
    showScreen('dashboard');
  }
  
  function loginWithEmail() {
    verifyOTP(); // Skip straight to login for demo
  }
  
  function logout() {
    document.getElementById('login-fullscreen').style.display = 'flex';
    document.getElementById('main-sidebar').style.display = 'none';
    document.getElementById('main-content').style.display = 'none';
    document.getElementById('login-step-0').classList.remove('hidden');
    document.getElementById('login-step-1').classList.add('hidden');
    document.getElementById('login-step-2').classList.add('hidden');
  }

  function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.sidebar a').forEach(a => a.classList.remove('active'));
    
    const targetScreen = document.getElementById('screen-' + screenId);
    if(targetScreen) {
      targetScreen.classList.add('active');
    }
    const targetNav = document.getElementById('nav-' + screenId);
    if(targetNav) {
      targetNav.classList.add('active');
    }
  }

  function openModal(id) { 
      const modal = document.getElementById(id);
      if(modal) modal.style.display = 'flex'; 
  }
  function closeModal(id) { 
      const modal = document.getElementById(id);
      if(modal) modal.style.display = 'none'; 
  }
  
  function startNewClaim() {
    showScreen('new-claim');
    claimNext(1);
    if(window.selectedAccountType === 'corporate') {
        document.getElementById('corporate-fast-track').classList.remove('hidden');
    } else {
        document.getElementById('corporate-fast-track').classList.add('hidden');
    }
  }

  function claimNext(step) {
    document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('[id^="claim-step-"]').forEach(s => s.classList.add('hidden'));
    
    const stepEl = document.getElementById('step' + step);
    if(stepEl) stepEl.classList.add('active');
    
    const claimStepEl = document.getElementById('claim-step-' + step);
    if(claimStepEl) claimStepEl.classList.remove('hidden');
    
    for(let i=1; i<step; i++) {
      const prevStep = document.getElementById('step' + i);
      if(prevStep) prevStep.classList.add('done');
    }
  }

  function switchTab(group, tabId) {
    const tabBtns = document.querySelectorAll(`[onclick^="switchTab('${group}'"]`);
    tabBtns.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    
    const contents = document.querySelectorAll(`[id^="${group}-"]`);
    contents.forEach(c => c.classList.remove('active'));
    document.getElementById(`${group}-${tabId}`).classList.add('active');
  }
// Toast Notification System
function showToast(message, type = 'success') {
  const container = document.getElementById('toast-container');
  if (!container) return;
  
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `<span>${message}</span>`;
  
  container.appendChild(toast);
  
  setTimeout(() => {
    toast.classList.add('fadeOut');
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

// Override alert for the scope of these forms (optional, but finding exact replaces is better)
window.submitClaim = function() {
  showToast('Claim submitted successfully!', 'success');
  claimNext(1);
  closeModal('screen-new-claim');
}

// Enforce minimum date on date inputs to prevent past date selection (Heuristic Fix)
document.addEventListener('DOMContentLoaded', () => {
    lucide.createIcons();
    const today = new Date().toISOString().split('T')[0];
    document.querySelectorAll('input[type="date"]').forEach(input => {
        // Only restrict if the input doesn't already have a value set in the past for demo purposes
        if (!input.value) {
            input.setAttribute('min', today);
        }
    });
});
