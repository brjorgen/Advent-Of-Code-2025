;; Yikes!

(defun read-file-into-grid (filename)
  "Read a text file into a list of strings (rows)."
  (with-open-file (in filename)
    (loop for line = (read-line in nil)
          while line
          collect line)))

(defun count-at-neighbors (grid row col)
  "Count @ symbols around the cell at (row, col)."
  (let ((rows (length grid))
        (cols (length (first grid)))
        (count 0))
    (loop for dr from -1 to 1 do
      (loop for dc from -1 to 1 do
        (unless (and (= dr 0) (= dc 0)) ; skip the center
          (let ((r (+ row dr))
                (c (+ col dc)))
            (when (and (>= r 0) (< r rows)
                       (>= c 0) (< c cols)
                       (char= (char (nth r grid) c) #\@))
              (incf count))))))
    count))

(defun count-rolls (grid)
  "Count @ symbols with fewer than 4 neighbors."
  (let ((rows (length grid))
        (cols (length (first grid)))
        (total 0))
    (loop for r from 0 below rows do
      (loop for c from 0 below cols do
        (when (char= (char (nth r grid) c) #\@)
          (when (< (count-at-neighbors grid r c) 4)
            (incf total)))))
    total))

(defun count-rolls-in-file (filename)
  (let ((grid (read-file-into-grid filename)))
    (count-rolls grid)))

(count-rolls-in-file "input.txt")
