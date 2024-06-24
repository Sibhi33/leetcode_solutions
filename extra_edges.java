{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf0 \expnd0\expndtw0\kerning0
class Solution \{\
        public int minKBitFlips(int[] A, int K) \{\
        int n = A.length, flipped = 0, res = 0;\
        int[] fp = new int[n];\
        for (int i = 0; i < A.length; ++i) \{\
            if (i >= K)\
                flipped ^= fp[i - K];\
            if (flipped == A[i]) \{\
                if (i + K > A.length)\
                    return -1;\
                fp[i] = 1;\
                flipped ^= 1;\
                res++;\
            \}\
        \}\
        return res;\
    \}\
\}}