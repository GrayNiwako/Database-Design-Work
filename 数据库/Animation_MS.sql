USE [master]
GO
/****** Object:  Database [Animation_MS]    Script Date: 2018/7/2 21:26:32 ******/
CREATE DATABASE [Animation_MS]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'动画信息管理系统', FILENAME = N'D:\Program Files\Microsoft SQL Server\MSSQL14.SQLEXPRESS\MSSQL\DATA\动画信息管理系统.mdf' , SIZE = 73728KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'动画信息管理系统_log', FILENAME = N'D:\Program Files\Microsoft SQL Server\MSSQL14.SQLEXPRESS\MSSQL\DATA\动画信息管理系统_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
GO
ALTER DATABASE [Animation_MS] SET COMPATIBILITY_LEVEL = 140
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Animation_MS].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Animation_MS] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Animation_MS] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Animation_MS] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Animation_MS] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Animation_MS] SET ARITHABORT OFF 
GO
ALTER DATABASE [Animation_MS] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Animation_MS] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Animation_MS] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Animation_MS] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Animation_MS] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Animation_MS] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Animation_MS] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Animation_MS] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Animation_MS] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Animation_MS] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Animation_MS] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Animation_MS] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Animation_MS] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Animation_MS] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Animation_MS] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Animation_MS] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Animation_MS] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Animation_MS] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [Animation_MS] SET  MULTI_USER 
GO
ALTER DATABASE [Animation_MS] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Animation_MS] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Animation_MS] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Animation_MS] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Animation_MS] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Animation_MS] SET QUERY_STORE = OFF
GO
USE [Animation_MS]
GO
ALTER DATABASE SCOPED CONFIGURATION SET IDENTITY_CACHE = ON;
GO
ALTER DATABASE SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = OFF;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET LEGACY_CARDINALITY_ESTIMATION = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 0;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET MAXDOP = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET PARAMETER_SNIFFING = ON;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET PARAMETER_SNIFFING = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = OFF;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET QUERY_OPTIMIZER_HOTFIXES = PRIMARY;
GO
USE [Animation_MS]
GO
/****** Object:  UserDefinedFunction [dbo].[getsinger]    Script Date: 2018/7/2 21:26:32 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--drop function getsinger
create function [dbo].[getsinger](@音乐 nvarchar(60))
returns @音乐及歌手 table
(
	歌手 nvarchar(255)
)
	begin
		insert @音乐及歌手
			select 姓名 as 歌手
			from 演唱
			where 音乐 = @音乐
		return
	end
GO
/****** Object:  Table [dbo].[音乐]    Script Date: 2018/7/2 21:26:32 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[音乐](
	[名称] [nvarchar](60) NOT NULL,
	[类型] [nvarchar](5) NOT NULL,
	[动画] [nvarchar](40) NOT NULL,
 CONSTRAINT [PK_音乐] PRIMARY KEY CLUSTERED 
(
	[名称] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[动画音乐列表]    Script Date: 2018/7/2 21:26:32 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[动画音乐列表]
as
select 音乐.动画,音乐.类型,音乐.名称,stuff((
	select '、'+歌手
	from getsinger(音乐.名称)
	for xml path('')),1,1,'') as 歌手
from 音乐
GO
/****** Object:  Table [dbo].[staff]    Script Date: 2018/7/2 21:26:32 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[staff](
	[姓名] [nvarchar](30) NOT NULL,
	[代表作] [nvarchar](80) NULL,
 CONSTRAINT [PK_staff] PRIMARY KEY CLUSTERED 
(
	[姓名] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[制作]    Script Date: 2018/7/2 21:26:32 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[制作](
	[姓名] [nvarchar](30) NOT NULL,
	[动画] [nvarchar](40) NOT NULL,
	[职位] [nvarchar](30) NOT NULL,
 CONSTRAINT [PK_制作] PRIMARY KEY CLUSTERED 
(
	[姓名] ASC,
	[动画] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[动画制作组列表]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[动画制作组列表]
as
select 制作.动画,制作.职位,制作.姓名,staff.代表作
from 制作,staff
where 制作.姓名 = staff.姓名
GO
/****** Object:  Table [dbo].[动画]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[动画](
	[名称] [nvarchar](40) NOT NULL,
	[制作类型] [nvarchar](6) NOT NULL,
	[改编类型] [nvarchar](8) NOT NULL,
	[原作公司] [nvarchar](30) NULL,
	[原作者] [nvarchar](30) NULL,
	[制作公司] [nvarchar](30) NOT NULL,
	[新番季度] [nvarchar](10) NOT NULL,
	[首播时间] [date] NOT NULL,
	[总集数] [smallint] NOT NULL,
 CONSTRAINT [PK_动画] PRIMARY KEY CLUSTERED 
(
	[名称] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[带年份的动画表]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[带年份的动画表]
as
select *,left(动画.新番季度,4) as 年份
from 动画
GO
/****** Object:  View [dbo].[限制时间]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[限制时间]
as
(select distinct 新番季度 as 限制时间
from 带年份的动画表)
union
(select distinct 年份 as 限制时间
from 带年份的动画表)
GO
/****** Object:  View [dbo].[季番表]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[季番表]
as
select *
from 带年份的动画表
where 总集数 <= 14
GO
/****** Object:  View [dbo].[半年番表]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[半年番表]
as
select *
from 带年份的动画表
where 总集数 > 14 and 总集数 <= 26
GO
/****** Object:  View [dbo].[长篇表]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[长篇表]
as
select *
from 带年份的动画表
where 总集数 > 26
GO
/****** Object:  View [dbo].[制作组动画人设表]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[制作组动画人设表]
as
select 姓名,代表作,动画制作组列表.动画,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数,年份
from 动画制作组列表,带年份的动画表
where 职位 like '%动画人设%' and 动画制作组列表.动画 = 带年份的动画表.名称
GO
/****** Object:  View [dbo].[制作组音乐表]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[制作组音乐表]
as
select 姓名,代表作,动画制作组列表.动画,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数,年份
from 动画制作组列表,带年份的动画表
where 职位 like '%音乐%' and 动画制作组列表.动画 = 带年份的动画表.名称
GO
/****** Object:  View [dbo].[制作组编剧表]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[制作组编剧表]
as
select 姓名,代表作,动画制作组列表.动画,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数,年份
from 动画制作组列表,带年份的动画表
where 职位 like '%编剧%' and 动画制作组列表.动画 = 带年份的动画表.名称
GO
/****** Object:  View [dbo].[制作组导演表]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[制作组导演表]
as
select 姓名,代表作,动画制作组列表.动画,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数,年份
from 动画制作组列表,带年份的动画表
where 职位 like '%导演%' and 动画制作组列表.动画 = 带年份的动画表.名称
GO
/****** Object:  Table [dbo].[人物]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[人物](
	[姓名] [nvarchar](30) NOT NULL,
	[性别] [nvarchar](6) NULL,
	[出生日期] [nvarchar](30) NULL,
	[职业] [nvarchar](20) NOT NULL,
	[代表作] [nvarchar](80) NULL,
 CONSTRAINT [PK_人物] PRIMARY KEY CLUSTERED 
(
	[姓名] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[cast]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cast](
	[姓名] [nvarchar](30) NOT NULL,
	[动画] [nvarchar](40) NOT NULL,
	[角色] [nvarchar](40) NOT NULL,
 CONSTRAINT [PK_cast] PRIMARY KEY CLUSTERED 
(
	[姓名] ASC,
	[动画] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[动画配音列表]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[动画配音列表]
as
select cast.动画,cast.角色,cast.姓名,人物.代表作
from cast,人物
where cast.姓名 = 人物.姓名
GO
/****** Object:  View [dbo].[声优配过的动画及信息]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[声优配过的动画及信息]
as
select 姓名,角色,名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数,年份
from 动画配音列表,带年份的动画表
where 动画配音列表.动画 = 带年份的动画表.名称
GO
/****** Object:  Table [dbo].[演唱]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[演唱](
	[姓名] [nvarchar](30) NOT NULL,
	[音乐] [nvarchar](60) NOT NULL,
 CONSTRAINT [PK_演唱] PRIMARY KEY CLUSTERED 
(
	[姓名] ASC,
	[音乐] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[歌手演唱动画信息]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[歌手演唱动画信息]
as
select distinct 演唱.姓名,带年份的动画表.名称,制作类型,改编类型,原作公司,原作者,制作公司,新番季度,首播时间,总集数,年份
from 音乐,演唱,带年份的动画表
where 音乐.名称 = 演唱.音乐 and 音乐.动画 = 带年份的动画表.名称
GO
/****** Object:  Table [dbo].[动画类别]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[动画类别](
	[名称] [nvarchar](40) NOT NULL,
	[类别] [nvarchar](10) NOT NULL,
 CONSTRAINT [PK_动画类别] PRIMARY KEY CLUSTERED 
(
	[名称] ASC,
	[类别] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[类别动画类别]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[类别动画类别]
as
select a1.类别 as 类别1,a1.名称,a2.类别 as 类别2
from 动画类别 as a1,动画类别 as a2
where a1.名称 = a2.名称
GO
/****** Object:  Table [dbo].[原作公司]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[原作公司](
	[名称] [nvarchar](30) NOT NULL,
	[地址] [nvarchar](60) NULL,
	[成立时间] [nvarchar](30) NULL,
	[主要业务] [nvarchar](80) NULL,
	[代表作] [nvarchar](80) NULL,
 CONSTRAINT [PK_原作公司] PRIMARY KEY CLUSTERED 
(
	[名称] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[原作公司被动画化作品]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[原作公司被动画化作品]
as
select 原作公司.名称,地址,成立时间,主要业务,代表作,带年份的动画表.名称 as 动画,改编类型,新番季度,年份
from 原作公司,带年份的动画表
where 原作公司.名称 = 带年份的动画表.原作公司
GO
/****** Object:  Table [dbo].[动画公司]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[动画公司](
	[名称] [nvarchar](30) NOT NULL,
	[地址] [nvarchar](60) NULL,
	[成立时间] [nvarchar](30) NULL,
	[代表作] [nvarchar](80) NULL,
 CONSTRAINT [PK_动画公司] PRIMARY KEY CLUSTERED 
(
	[名称] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[动画公司制作作品]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[动画公司制作作品]
as
select 动画公司.名称,地址,成立时间,代表作,带年份的动画表.名称 as 动画,新番季度,年份
from 动画公司,带年份的动画表
where 动画公司.名称 = 带年份的动画表.制作公司
GO
/****** Object:  View [dbo].[声优参与动画]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[声优参与动画]
as
select 人物.姓名,性别,出生日期,代表作,新番季度,count(*) as 参与数量
from 动画,人物,cast
where 动画.名称 = cast.动画 and cast.姓名 = 人物.姓名
group by 人物.姓名,性别,出生日期,代表作,新番季度
GO
/****** Object:  View [dbo].[歌手组合参与动画]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[歌手组合参与动画]
as
select 人物.姓名,性别,出生日期,代表作,新番季度,count(*) as 参与数量
from 动画,人物,音乐,演唱
where 音乐.名称 = 演唱.音乐 and 演唱.姓名 = 人物.姓名 and 音乐.动画 = 动画.名称
group by 人物.姓名,性别,出生日期,代表作,新番季度
GO
/****** Object:  View [dbo].[原作作者参与动画]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[原作作者参与动画]
as
select 人物.姓名,性别,出生日期,代表作,改编类型,新番季度,count(*) as 参与数量
from 动画,人物
where 动画.原作者 = 人物.姓名
group by 人物.姓名,性别,出生日期,代表作,改编类型,新番季度
GO
/****** Object:  View [dbo].[staff参与动画]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[staff参与动画]
as
select 姓名,代表作,动画,职位,新番季度,年份
from 动画制作组列表,带年份的动画表
where 动画制作组列表.动画 = 带年份的动画表.名称
GO
/****** Object:  View [dbo].[季度新番动画音乐]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[季度新番动画音乐]
as
select 动画音乐列表.名称,类型,动画,歌手,新番季度
from 动画音乐列表,动画
where 动画音乐列表.动画 = 动画.名称
GO
/****** Object:  View [dbo].[演唱动画音乐]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[演唱动画音乐]
as
select 演唱.姓名,动画音乐列表.名称,类型,动画,歌手,新番季度,年份
from 动画音乐列表,演唱,带年份的动画表
where 动画音乐列表.动画 = 带年份的动画表.名称 and 演唱.音乐 = 动画音乐列表.名称
GO
/****** Object:  View [dbo].[动画基本信息]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[动画基本信息]
as
(select 动画.名称,动画.制作类型,动画.改编类型,动画.原作公司,原作公司.代表作 as 原作公司代表作,动画.原作者,
	人物.代表作 as 原作者代表作,动画.制作公司,动画公司.代表作 as 制作公司代表作,动画.新番季度,动画.首播时间,动画.总集数
from 动画,原作公司,人物,动画公司
where 动画.原作公司 = 原作公司.名称 and 动画.原作者 = 人物.姓名 and 动画.制作公司 = 动画公司.名称)
union
(select 动画.名称,动画.制作类型,动画.改编类型,动画.原作公司,原作公司.代表作 as 原作公司代表作,动画.原作者,
	null as 原作者代表作,动画.制作公司,动画公司.代表作 as 制作公司代表作,动画.新番季度,动画.首播时间,动画.总集数
from 动画,原作公司,动画公司
where 动画.原作公司 = 原作公司.名称 and 动画.原作者 is null and 动画.制作公司 = 动画公司.名称)
union
(select 动画.名称,动画.制作类型,动画.改编类型,动画.原作公司,null as 原作公司代表作,动画.原作者,
	null as 原作者代表作,动画.制作公司,动画公司.代表作 as 制作公司代表作,动画.新番季度,动画.首播时间,动画.总集数
from 动画,动画公司
where 动画.改编类型 = '原创' and 动画.制作公司 = 动画公司.名称)
GO
/****** Object:  View [dbo].[每季度番剧数量]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[每季度番剧数量]
as
with type1 as
	(select 新番季度,count(*) as 新作数量 from 动画 where 制作类型 = '新作' group by 新番季度),
	type2 as
	(select 新番季度,count(*) as 续作数量 from 动画 where 制作类型 = '续作' group by 新番季度),
	type3 as
	(select 新番季度,count(*) as 衍生数量 from 动画 where 制作类型 = '衍生' group by 新番季度),
	type4 as
	(select 新番季度,count(*) as 重制数量 from 动画 where 制作类型 = '重制' group by 新番季度),
	type5 as
	(select 新番季度,count(*) as 漫改数量 from 动画 where 改编类型 = '漫改' group by 新番季度),
	type6 as
	(select 新番季度,count(*) as 轻改数量 from 动画 where 改编类型 = '轻改' group by 新番季度),
	type7 as
	(select 新番季度,count(*) as 游戏改数量 from 动画 where 改编类型 = '游戏改' group by 新番季度),
	type8 as
	(select 新番季度,count(*) as 原创数量 from 动画 where 改编类型 = '原创' group by 新番季度),
	total as
	(select type1.新番季度,
		case when type1.新作数量 is not null then type1.新作数量 else 0 end as 新作数量,
		case when type2.续作数量 is not null then type2.续作数量 else 0 end as 续作数量,
		case when type3.衍生数量 is not null then type3.衍生数量 else 0 end as 衍生数量,
		case when type4.重制数量 is not null then type4.重制数量 else 0 end as 重制数量,
		case when type5.漫改数量 is not null then type5.漫改数量 else 0 end as 漫改数量,
		case when type6.轻改数量 is not null then type6.轻改数量 else 0 end as 轻改数量,
		case when type7.游戏改数量 is not null then type7.游戏改数量 else 0 end as 游戏改数量,
		case when type8.原创数量 is not null then type8.原创数量 else 0 end as 原创数量
	from type1 full outer join type2 on type1.新番季度 = type2.新番季度
		full outer join type3 on type1.新番季度 = type3.新番季度
		full outer join type4 on type1.新番季度 = type4.新番季度
		full outer join type5 on type1.新番季度 = type5.新番季度
		full outer join type6 on type1.新番季度 = type6.新番季度
		full outer join type7 on type1.新番季度 = type7.新番季度
		full outer join type8 on type1.新番季度 = type8.新番季度)
select 新番季度,(新作数量+续作数量+衍生数量+重制数量) as 番剧数量,新作数量,续作数量,衍生数量,重制数量,
	漫改数量,轻改数量,游戏改数量,原创数量
from total
GO
ALTER TABLE [dbo].[动画] ADD  CONSTRAINT [DF_动画_总集数]  DEFAULT ((0)) FOR [总集数]
GO
ALTER TABLE [dbo].[cast]  WITH CHECK ADD  CONSTRAINT [FK_cast_动画] FOREIGN KEY([动画])
REFERENCES [dbo].[动画] ([名称])
GO
ALTER TABLE [dbo].[cast] CHECK CONSTRAINT [FK_cast_动画]
GO
ALTER TABLE [dbo].[cast]  WITH CHECK ADD  CONSTRAINT [FK_cast_人物] FOREIGN KEY([姓名])
REFERENCES [dbo].[人物] ([姓名])
GO
ALTER TABLE [dbo].[cast] CHECK CONSTRAINT [FK_cast_人物]
GO
ALTER TABLE [dbo].[动画]  WITH CHECK ADD  CONSTRAINT [FK_动画_人物] FOREIGN KEY([原作者])
REFERENCES [dbo].[人物] ([姓名])
GO
ALTER TABLE [dbo].[动画] CHECK CONSTRAINT [FK_动画_人物]
GO
ALTER TABLE [dbo].[动画]  WITH CHECK ADD  CONSTRAINT [FK_动画_原作公司] FOREIGN KEY([原作公司])
REFERENCES [dbo].[原作公司] ([名称])
GO
ALTER TABLE [dbo].[动画] CHECK CONSTRAINT [FK_动画_原作公司]
GO
ALTER TABLE [dbo].[动画]  WITH CHECK ADD  CONSTRAINT [FK_动画_制作公司] FOREIGN KEY([制作公司])
REFERENCES [dbo].[动画公司] ([名称])
GO
ALTER TABLE [dbo].[动画] CHECK CONSTRAINT [FK_动画_制作公司]
GO
ALTER TABLE [dbo].[动画类别]  WITH CHECK ADD  CONSTRAINT [FK_动画类别_动画] FOREIGN KEY([名称])
REFERENCES [dbo].[动画] ([名称])
GO
ALTER TABLE [dbo].[动画类别] CHECK CONSTRAINT [FK_动画类别_动画]
GO
ALTER TABLE [dbo].[演唱]  WITH CHECK ADD  CONSTRAINT [FK_演唱_人物] FOREIGN KEY([姓名])
REFERENCES [dbo].[人物] ([姓名])
GO
ALTER TABLE [dbo].[演唱] CHECK CONSTRAINT [FK_演唱_人物]
GO
ALTER TABLE [dbo].[演唱]  WITH CHECK ADD  CONSTRAINT [FK_演唱_音乐] FOREIGN KEY([音乐])
REFERENCES [dbo].[音乐] ([名称])
GO
ALTER TABLE [dbo].[演唱] CHECK CONSTRAINT [FK_演唱_音乐]
GO
ALTER TABLE [dbo].[音乐]  WITH CHECK ADD  CONSTRAINT [FK_音乐_动画] FOREIGN KEY([动画])
REFERENCES [dbo].[动画] ([名称])
GO
ALTER TABLE [dbo].[音乐] CHECK CONSTRAINT [FK_音乐_动画]
GO
ALTER TABLE [dbo].[制作]  WITH CHECK ADD  CONSTRAINT [FK_制作_staff] FOREIGN KEY([姓名])
REFERENCES [dbo].[staff] ([姓名])
GO
ALTER TABLE [dbo].[制作] CHECK CONSTRAINT [FK_制作_staff]
GO
ALTER TABLE [dbo].[制作]  WITH CHECK ADD  CONSTRAINT [FK_制作_动画] FOREIGN KEY([动画])
REFERENCES [dbo].[动画] ([名称])
GO
ALTER TABLE [dbo].[制作] CHECK CONSTRAINT [FK_制作_动画]
GO
ALTER TABLE [dbo].[动画]  WITH CHECK ADD  CONSTRAINT [adapted_type] CHECK  ((case when [改编类型]='原创' then case when [原作公司] IS NULL AND [原作者] IS NULL then (1) else (0) end when [改编类型]='游戏改' then case when [原作公司] IS NOT NULL then (1) else (0) end else case when [原作公司] IS NOT NULL AND [原作者] IS NOT NULL then (1) else (0) end end=(1)))
GO
ALTER TABLE [dbo].[动画] CHECK CONSTRAINT [adapted_type]
GO
ALTER TABLE [dbo].[动画]  WITH CHECK ADD  CONSTRAINT [CK_动画_改编类型] CHECK  (([改编类型]='漫改' OR [改编类型]='轻改' OR [改编类型]='游戏改' OR [改编类型]='原创'))
GO
ALTER TABLE [dbo].[动画] CHECK CONSTRAINT [CK_动画_改编类型]
GO
ALTER TABLE [dbo].[动画]  WITH CHECK ADD  CONSTRAINT [CK_动画_新番季度] CHECK  (([新番季度] like '[0-9][0-9][0-9][0-9]年[春夏秋冬]'))
GO
ALTER TABLE [dbo].[动画] CHECK CONSTRAINT [CK_动画_新番季度]
GO
ALTER TABLE [dbo].[动画]  WITH CHECK ADD  CONSTRAINT [CK_动画_制作类型] CHECK  (([制作类型]='新作' OR [制作类型]='续作' OR [制作类型]='衍生' OR [制作类型]='重制'))
GO
ALTER TABLE [dbo].[动画] CHECK CONSTRAINT [CK_动画_制作类型]
GO
ALTER TABLE [dbo].[动画]  WITH CHECK ADD  CONSTRAINT [CK_动画_总集数] CHECK  (([总集数]>=(0)))
GO
ALTER TABLE [dbo].[动画] CHECK CONSTRAINT [CK_动画_总集数]
GO
ALTER TABLE [dbo].[人物]  WITH CHECK ADD  CONSTRAINT [CK_人物_性别] CHECK  (([性别]='男' OR [性别]='女' OR [性别]=NULL))
GO
ALTER TABLE [dbo].[人物] CHECK CONSTRAINT [CK_人物_性别]
GO
ALTER TABLE [dbo].[音乐]  WITH CHECK ADD  CONSTRAINT [CK_音乐_类型] CHECK  (([类型]='ED' OR [类型]='OP'))
GO
ALTER TABLE [dbo].[音乐] CHECK CONSTRAINT [CK_音乐_类型]
GO
ALTER TABLE [dbo].[制作]  WITH CHECK ADD  CONSTRAINT [CK_制作_职位] CHECK  (([职位]='导演、编剧、音乐、动画人设' OR [职位]='编剧、音乐、动画人设' OR [职位]='导演、音乐、动画人设' OR [职位]='导演、编剧、动画人设' OR [职位]='导演、编剧、音乐' OR [职位]='音乐、动画人设' OR [职位]='编剧、动画人设' OR [职位]='编剧、音乐' OR [职位]='导演、动画人设' OR [职位]='导演、音乐' OR [职位]='导演、编剧' OR [职位]='动画人设' OR [职位]='音乐' OR [职位]='编剧' OR [职位]='导演'))
GO
ALTER TABLE [dbo].[制作] CHECK CONSTRAINT [CK_制作_职位]
GO
/****** Object:  StoredProcedure [dbo].[pr_删除音乐时级联删除演唱]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create procedure [dbo].[pr_删除音乐时级联删除演唱]
	@音乐 nvarchar(60)
as
begin
	delete from 演唱 where 音乐=@音乐
	delete from 音乐 where 名称=@音乐
end
GO
/****** Object:  Trigger [dbo].[删除动画时的级联删除]    Script Date: 2018/7/2 21:26:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create trigger [dbo].[删除动画时的级联删除]
	on [dbo].[动画]
	instead of delete
as
begin
	declare @动画 nvarchar(40)
	set @动画 = (select 名称 from deleted)
	delete from 动画类别 where 名称=@动画
	delete from cast where 动画=@动画
	delete from 演唱 where exists
		(select 名称 from 音乐 where 演唱.音乐 = 音乐.名称 and 动画=@动画)
	delete from 音乐 where 动画=@动画
	delete from 动画 where 名称=@动画
end
GO
ALTER TABLE [dbo].[动画] ENABLE TRIGGER [删除动画时的级联删除]
GO
USE [master]
GO
ALTER DATABASE [Animation_MS] SET  READ_WRITE 
GO
