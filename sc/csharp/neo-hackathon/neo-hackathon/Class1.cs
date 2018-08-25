using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using Neo.SmartContract.Framework.Services.System;
using System;
using System.Linq;
using System.ComponentModel;
using System.Numerics;

namespace Neo.SmartContract
{
    public class ICO_Template : Framework.SmartContract
    {

        //Token Settings
        public static string Name() => "SanchoCoin";
        public static string Symbol() => "SAN";
        public static readonly byte[] Owner = "AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y".ToScriptHash();
        public static byte Decimals() => 8;
        private const ulong factor = 100000000; //decided by Decimals()
        private const ulong neo_decimals = 100000000;

        //ICO Settings
        private static readonly byte[] neo_asset_id = { 155, 124, 255, 218, 166, 116, 190, 174, 15, 147, 14, 190, 96, 133, 175, 144, 147, 229, 254, 86, 179, 74, 92, 34, 12, 205, 207, 110, 252, 51, 111, 197 };

        public delegate void MyAction<T, T1, T2>(T p0, T1 p1, T2 p2);

        [DisplayName("transfer")]
        public static event MyAction<byte[], byte[], BigInteger> Transferred;

        public static Object Main(string operation, params object[] args)
        {
            if (operation == "claimTokens") return ClaimTokens();
            if (operation == "name") return Name();
            if (operation == "symbol") return Symbol();
            if (operation == "decimals") return Decimals();
            if (operation == "balanceOf")
            {
                if (args.Length != 1) return 0;
                byte[] account = (byte[])args[0];
                return BalanceOf(account);
            }
            if (operation == "totalSupply") return TotalSupply();
            if (operation == "upload") {
                if (args.Length != 1) return false;
                byte[] data = (byte[])args[0];
                return Upload(data);
            }

            return false;
        }

        public static bool ClaimTokens()
        {
            byte[] sender = GetSender();
            // contribute asset is not neo
            if (sender.Length == 0)
            {
                return false;
            }
            BigInteger balance = Storage.Get(Storage.CurrentContext, sender).AsBigInteger();
            if (balance > 0) return false;
            Storage.Put(Storage.CurrentContext, sender, 1 + balance);
            BigInteger totalSupply = Storage.Get(Storage.CurrentContext, "totalSupply").AsBigInteger();
            Storage.Put(Storage.CurrentContext, "totalSupply", 1 + totalSupply);
            Transferred(null, sender, 1);
            return true;
        }

        public static BigInteger TotalSupply()
        {
            return Storage.Get(Storage.CurrentContext, "totalSupply").AsBigInteger();
        }

        public static BigInteger BalanceOf(byte[] address)
        {
            return Storage.Get(Storage.CurrentContext, address).AsBigInteger();
        }

        // Upload Book Information
        public static Object Upload(byte[] data)
        {
            byte[] sender = GetSender();
            if (sender.Length == 0)
            {
                return false;
            }
            Storage.Put(Storage.CurrentContext, "a", data);
            
            return Storage.Get(Storage.CurrentContext, "a").AsString();
        }

        //// Get Book
        //public static string GetContent(string id)
        //{
        //    string result = Storage.Get(Storage.CurrentContext, id).AsString();

        //    if (result.Length != 0)
        //    {
        //        return result;
        //    }

        //    return "";
        //}

        //// Get All Book List
        //public static string[] ListContent()
        //{
        //    BigInteger idcount = Storage.Get(Storage.CurrentContext, "ids\x00count").AsBigInteger();
        //    if (idcount == 0)
        //    {
        //        return new string[0];
        //    }

        //    string[] result = new string[(Int64)idcount];

        //    for (int i = 0; i < idcount; i++){
        //        result[i] = Storage.Get(Storage.CurrentContext, "ids\x00" + (i + 1)).AsString();
        //    }

        //    if (result.Length != 0) {
        //        return result;
        //    }

        //    return new string[0];
        //}

        // check whether asset is neo and get sender script hash
        private static byte[] GetSender()
        {
            Transaction tx = (Transaction)ExecutionEngine.ScriptContainer;
            TransactionOutput[] reference = tx.GetReferences();
            // you can choice refund or not refund
            foreach (TransactionOutput output in reference)
            {
                return output.ScriptHash;
            }
            return new byte[] { };
        }

        public static byte[] Combine(Book book)
        {
            return book.Path.Concat(book.Name).Concat(book.Sender);
        }

        public static string GetID(Book book)
        {
            return Sha256(Combine(book)).AsString();
        }

    }
}