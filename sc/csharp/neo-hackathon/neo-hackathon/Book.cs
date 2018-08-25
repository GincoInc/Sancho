namespace Neo.SmartContract
{
    public struct Book
    {
        public byte[] Path; //ipfsのパス
        public byte[] Name; //書名
        public byte[] Sender; //投稿者
        public byte[] Author; //著者
        public int PV; //本のPV数
    }
}