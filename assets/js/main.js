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
    document.querySelectorAll('.login-method-btn').forEach(el => el.classList.remove('active', 'antd-btn-primary'));
    
    // Add default button style back to all
    document.querySelectorAll('.login-method-btn').forEach(el => {
      if(!el.classList.contains('active')) el.style.background = 'transparent';
    });
    
    const activeBtn = document.getElementById('method-' + method);
    if(activeBtn) {
      activeBtn.classList.add('active', 'antd-btn-primary');
      activeBtn.style.background = ''; // reset inline style to let primary class work
    }
    
    document.querySelectorAll('.login-form').forEach(el => el.classList.add('hidden'));
    
    const activeForm = document.getElementById('login-' + method);
    if(activeForm) activeForm.classList.remove('hidden');
  }

  function sendOTP(method) {
    document.getElementById('login-step-1').classList.add('hidden');
    document.getElementById('login-step-2').classList.remove('hidden');
    
    let dest = '';
    if(method === 'phone') dest = document.getElementById('phone-input').value || '+91 98765 43210';
    if(method === 'aadhaar') {
      const aadhaar = document.getElementById('aadhaar-input').value || 'XXXX XXXX XXXX';
      dest = 'Aadhaar ' + aadhaar + ' linked number';
    }
    if(method === 'employee-id') dest = document.getElementById('employee-id-input').value || 'Corporate SSO';
    
    document.getElementById('otp-destination').innerHTML = dest;
    
    // Auto focus first OTP input
    setTimeout(() => { document.getElementById('otp-1').focus(); }, 100);
  }

  // Handle auto-advancing OTP
  window.moveToNextOTP = function(currentInput, nextInputId) {
    if (currentInput.value.length >= 1 && nextInputId) {
      document.getElementById(nextInputId).focus();
    }
  };

  // Handle backspace in OTP
  window.handleOTPBackspace = function(e, currentInput, prevInputId) {
    if (e.key === 'Backspace' && currentInput.value === '' && prevInputId) {
      document.getElementById(prevInputId).focus();
    }
  };

  function verifyOTP() {
    document.getElementById('login-fullscreen').style.display = 'none';
    
    document.getElementById('app-container').style.display = 'flex';
    
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
    
    document.getElementById('app-container').style.display = 'none';
    document.getElementById('login-step-0').classList.remove('hidden');
    document.getElementById('login-step-1').classList.add('hidden');
    document.getElementById('login-step-2').classList.add('hidden');
  }

  function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.app-sidebar a').forEach(a => a.classList.remove('active'));
    
    const targetScreen = document.getElementById('screen-' + screenId);
    if(targetScreen) {
      targetScreen.classList.add('active');
      if (typeof lucide !== 'undefined') {
        lucide.createIcons({ root: targetScreen });
      }
    }
    const targetNav = document.getElementById('nav-' + screenId);
    if(targetNav) {
      targetNav.classList.add('active');
    }
  }

  function openModal(id) { 
      const modal = document.getElementById(id);
      if(modal) modal.classList.add('active'); 
  }
  function closeModal(id) { 
      const modal = document.getElementById(id);
      if(modal) modal.classList.remove('active'); 
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
    document.querySelectorAll('.antd-step-item').forEach(s => {
      s.classList.remove('active');
      s.classList.remove('done');
    });
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
  let container = document.getElementById('antd-message-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'antd-message-container';
    container.style.cssText = 'position: fixed; top: 80px; left: 50%; transform: translateX(-50%); z-index: 10000; display: flex; flex-direction: column; gap: 8px; pointer-events: none;';
    document.body.appendChild(container);
  }
  
  const icon = type === 'success' ? '<i data-lucide="check-circle" class="icon-sm" style="color: var(--antd-success);"></i>' : '<i data-lucide="alert-circle" class="icon-sm" style="color: var(--antd-error);"></i>';
  
  const toast = document.createElement('div');
  toast.style.cssText = 'background: white; padding: 10px 16px; border-radius: var(--antd-radius); box-shadow: 0 6px 16px 0 rgba(0,0,0,0.08); display: flex; align-items: center; gap: 8px; font-size: 14px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial; color: rgba(0,0,0,0.88); opacity: 0; transform: translateY(-20px); transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1); pointer-events: auto;';
  toast.innerHTML = `${icon}<span>${message}</span>`;
  
  container.appendChild(toast);
  
  if (typeof lucide !== 'undefined') {
    lucide.createIcons({ root: toast });
  }
  
  // Animate in
  setTimeout(() => {
    toast.style.opacity = '1';
    toast.style.transform = 'translateY(0)';
  }, 10);
  
  // Animate out
  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(-20px)';
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

// Override alert for the scope of these forms (optional, but finding exact replaces is better)
window.submitClaim = function() {
  showToast('Claim submitted successfully!', 'success');
  claimNext(1);
}

window.submitClaimFinal = function() {
  // Show success step
  document.querySelectorAll('[id^="claim-step-"]').forEach(s => s.classList.add('hidden'));
  document.getElementById('claim-step-5').classList.remove('hidden');
  
  // Mark all stepper steps as done
  document.querySelectorAll('.antd-step-item').forEach(s => {
    s.classList.remove('active');
    s.classList.add('done');
  });
  
  showToast('Claim #CLM-2026-0046 submitted successfully!', 'success');
  
  // Re-init icons for the success screen
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
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
