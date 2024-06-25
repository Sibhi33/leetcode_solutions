{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;\red30\green30\blue30;\red71\green137\blue205;
\red202\green202\blue202;\red67\green192\blue160;\red212\green213\blue154;\red141\green212\blue254;\red167\green197\blue151;
\red183\green111\blue179;\red238\green46\blue55;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c100000;\cssrgb\c15704\c15704\c15684;\cssrgb\c33936\c61427\c84130;
\cssrgb\c83229\c83229\c83125;\cssrgb\c30610\c78876\c69022;\cssrgb\c86261\c86245\c66529;\cssrgb\c61361\c86489\c99746;\cssrgb\c71008\c80807\c65805;
\cssrgb\c77331\c52624\c75301;\cssrgb\c95677\c27779\c27659;\cssrgb\c100000\c100000\c100000\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 class\cb3 \strokec5  \cb3 \strokec6 Solution\cb3 \strokec5 :\cb1 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec5     \cb3 \strokec4 def\cb3 \strokec5  \cb3 \strokec7 bstToGst\cb3 \strokec5 (\cb3 \strokec8 self\cb3 \strokec5 , \cb3 \strokec8 root\cb3 \strokec5 : TreeNode) -> TreeNode:\cb1 \strokec5 \
\cb3 \strokec5         \cb3 \strokec4 self\cb3 \strokec5 .val = \cb3 \strokec9 0\cb1 \strokec5 \
\cb3 \strokec5         \cb1 \strokec5 \
\cb3 \strokec5         \cb3 \strokec4 def\cb3 \strokec5  \cb3 \strokec7 dfs\cb3 \strokec5 (\cb3 \strokec8 node\cb3 \strokec5 ):\cb1 \strokec5 \
\cb3 \strokec5             \cb3 \strokec10 if\cb3 \strokec5  \cb3 \strokec4 not\cb3 \strokec5  node:\cb1 \strokec5 \
\cb3 \strokec5                 \cb3 \strokec10 return\cb1 \strokec5 \
\cb3 \strokec5             \cb1 \strokec5 \
\cb3 \strokec5             dfs(node.right)\cb1 \strokec5 \
\cb3 \strokec5             \cb3 \strokec4 self\cb3 \strokec5 .val += node.val\cb1 \strokec5 \
\cb3 \strokec5             node.val = \cb3 \strokec4 self\cb3 \strokec5 .val\cb1 \strokec5 \
\cb3 \strokec5             dfs(node.left)\cb1 \strokec5 \
\cb3 \strokec5         \cb1 \strokec5 \
\cb3 \strokec5         dfs(root)\cb1 \strokec5 \
\cb3 \strokec5         \cb3 \strokec10 return\cb3 \strokec5  root\cb3 \strokec11 ;\cf5 \cb12 \strokec5 \
}