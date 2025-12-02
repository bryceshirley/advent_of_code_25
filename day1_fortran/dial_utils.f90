module dial_utils
    implicit none
    private
    public :: turn_one_position, turn_dial, read_input
    public :: count_zero_lands_part1, count_zero_lands_part2

contains

    function turn_one_position(pos, direction) result(new_pos)
        integer, intent(in) :: pos ! intent(in) means this argument is read-only 
        character(len=1), intent(in) :: direction
        integer :: new_pos

        if (direction == 'L') then
            new_pos = modulo(pos - 1, 100)
        else if (direction == 'R') then
            new_pos = modulo(pos + 1, 100)
        else
            print *, "Error: Direction must be 'R' or 'L'."
            stop 1
        end if

    end function turn_one_position


    subroutine turn_dial(pos, turn_amount, direction, lands)
        integer, intent(inout) :: pos ! intent(inout) means this argument can be read and modified
        integer, intent(in) :: turn_amount
        character(len=1), intent(in) :: direction
        integer, intent(out) :: lands ! intent(out) means this argument is used to return a value
        integer :: i

        lands = 0
        do i = 1, turn_amount
            pos = turn_one_position(pos, direction)
            if (pos == 0) then
                lands = lands + 1
            end if
        end do
    end subroutine turn_dial


    subroutine read_input(file_path, lines, max_lines, n_lines)
        character(len=*), intent(in) :: file_path
        character(len=256), intent(out) :: lines(max_lines)
        integer, intent(in) :: max_lines
        integer, intent(out) :: n_lines

        integer :: unit_num, iostat, i
        character(len=256) :: buffer

        unit_num = 10
        n_lines = 0

        open(unit=unit_num, file=file_path, status='old', action='read', iostat=iostat)
        if (iostat /= 0) then
            print *, "Error: Could not open file ", trim(file_path)
            stop 1
        end if

        do i = 1, max_lines
            read(unit_num, '(A)', iostat=iostat) buffer
            if (iostat /= 0) exit
            lines(i) = trim(buffer)
            n_lines = n_lines + 1
        end do

        close(unit_num)
    end subroutine read_input


    function count_zero_lands_part1(lines, verbose_level) result(count)
        character(len=256), intent(in) :: lines(:)
        integer, intent(in) :: verbose_level
        integer :: count, pos, amount, i, lands
        character(len=1) :: direction
        character(len=256) :: line_str

        pos = 50
        count = 0

        if (verbose_level > 0) print *, "The dial starts by pointing at ", pos

        do i = 1, size(lines)
            line_str = trim(lines(i))
            if (len_trim(line_str) < 2) cycle

            direction = line_str(1:1)
            read(line_str(2:), *) amount

            call turn_dial(pos, amount, direction, lands)

            if (verbose_level > 0) &
                print *, "The dial is rotated ", trim(line_str), " to point at ", pos

            if (pos == 0) count = count + 1
        end do
    end function count_zero_lands_part1


    function count_zero_lands_part2(lines, verbose_level) result(count)
        character(len=256), intent(in) :: lines(:)
        integer, intent(in) :: verbose_level
        integer :: count, pos, amount, i, lands
        character(len=1) :: direction
        character(len=256) :: line_str
        character(len=256) :: stdout, lands_msg
        character(len=10) :: pos_str, lands_str

        pos = 50
        count = 0

        if (verbose_level > 0) print *, "The dial starts by pointing at ", pos

        do i = 1, size(lines)
            line_str = trim(lines(i))
            if (len_trim(line_str) < 2) cycle

            direction = line_str(1:1)
            read(line_str(2:), *) amount

            call turn_dial(pos, amount, direction, lands)

            if (verbose_level > 0) then
                write(pos_str, *) pos
                stdout = "The dial is rotated " // trim(line_str) // &
                         " to point at " // adjustl(trim(pos_str))

                lands_msg = ""
                if (lands > 0 .and. pos /= 0) then
                    write(lands_str, *) lands
                    lands_msg = "; during this rotation, the number of times it points at 0 is " // &
                                adjustl(trim(lands_str))
                end if

                print *, trim(stdout) // trim(lands_msg) // "."
            end if

            count = count + lands
        end do
    end function count_zero_lands_part2

end module dial_utils
