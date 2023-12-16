create table
    stu_info(
        sid char(4),
        name char(8),
        dept_name char(8),
        sex char(2),
        age char(2),
        SDEPT char(10),
        LOGN char(20),
        PSWD char(20),
        primary key(sid)
    );

create table dept_info( dept_name char(8) );

create table
    course(
        cid char(4),
        name char(8),
        teacher char(8),
        time char(8),
        classroom char(8),
        credit char(4)
    );

/* stu_course    考试管理 */

create table
    stu_course(
        sid char(4),
        stu_name char(4),
        cid char(4),
        course_name char(8),
        score char(8)
    );

UPDATE stu_course
SET
    sid = 's2',
    stu_name = '刘晓鸣',
    cid = 'c2',
    course_name = '计算机原理',
    score = '55'
WHERE `sid` = 's';

insert into stu_course values('s3','李明','c3','数据库原理','72');


/* exam_makeup */
create table
    exam_makeup(
        sid char(4),
        stu_name char(4),
        cid char(4),
        course_name char(8),
        score char(8)
        
    );

SET foreign_key_checks = 0