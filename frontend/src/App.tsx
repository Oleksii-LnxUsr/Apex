import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Footer from './Components/Footer/Footer';
import Home from './Page/Home';
import Staking from './Page/Staking';
import Referal from './Page/Referal';
import Contest from './Page/Contest';
import { TransactionsProvider } from './Components/TransactionsContext';
import Farming from './Page/Farming';
import Profile from './Page/Profile';
import Conclusioin from '././Page/Conclusion';
import Transfers from './Page/Transfers';
import useAuth from './Hooks/useAuth';
import { useEffect, useState, useLayoutEffect } from 'react';
import { TonConnectUIProvider } from '@tonconnect/ui-react';
import Deposite from './Page/Deposite';
import LoadingPage from './Components/LoadingPage/LoadingPage';

declare global {
  interface Window {
    Telegram: {
      WebApp: {
        initData: string;
      };
    };
  }
}

function App() {
  const { signIn, isAuth } = useAuth();
  const [initData, setInitData] = useState<string>('');
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
   if (window.Telegram && window.Telegram.WebApp) {
      const data = window.Telegram.WebApp.initData;
      
      if (data) {
        setInitData(data);
      }
    }
  }, [signIn]);

  const handleContinue = () => {
    sessionStorage.setItem('hasVisited', 'true');
    setIsLoading(false);
  };

  useLayoutEffect(() => {
    const hasVisited = sessionStorage.getItem('hasVisited');
    if (hasVisited) {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    if (initData) {
      console.log(initData)
      signIn(initData);
    }
  }, [initData]);


  if (isLoading) {
    return <LoadingPage onContinue={handleContinue} />;
  }

  return (
    <TonConnectUIProvider
      manifestUrl="https://apexstake.xyz/tonconnect-manifest.json"
      walletsRequiredFeatures={{
        sendTransaction: {
          minMessages: 2, // Кошелек должен поддерживать отправку хотя бы 2 сообщений
          extraCurrencyRequired: true, // Кошелек должен поддерживать дополнительную валюту в транзакциях
        },
      }}
    >
      <TransactionsProvider>
        <div className="app-container">
          <Router>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/staking" element={<Staking />} />
              <Route path="/referrals" element={<Referal />} />
              <Route path="/contest" element={<Contest />} />
              <Route path="/farming" element={<Farming />} />
              <Route path="/profile" element={<Profile />} />
              <Route path="/conclusioin" element={<Conclusioin />} />
              <Route path="/deposite" element={<Deposite />} />
              <Route path="/transfers" element={<Transfers />} />
            </Routes>
            <Footer />
          </Router>
        </div>
      </TransactionsProvider>
    </TonConnectUIProvider>
  );
}

export default App;
